# Create your views here.
from brainstorm.models import KeyWord
from brainstorm.forms import AddWordForm
from django.shortcuts import render_to_response
from random import randint




def index(request):
	
	total_words = KeyWord.objects.all().count()
	max_num = KeyWord.objects.all().order_by("-id")[0].id
	random_word_id = randint(1, max_num)
	random_word = KeyWord.objects.get(id=random_word_id)
	return render_to_response('index.html', {'random_word': random_word, 'total_words':total_words})
	
	
def showWord(request, key_word_id):
	
	# Get the word
	key_word = KeyWord.objects.get(id=int(key_word_id))
	
	# Deal with the Form
	if request.method == 'POST':
		form = AddWordForm(request.POST)
		if form.is_valid():
			word = form.cleaned_data['word']
			# Check if word exist
			if(KeyWord.objects.filter(word_name=word).count()):
				newWord = KeyWord.objects.get(word_name=word)
				key_word.related_word.add(newWord)
			else:
				# else create a new word
				w = KeyWord(word_name=word)
				w.save()
				key_word.related_word.add(KeyWord.objects.get(word_name=word))
			form = AddWordForm()
				
	else:
		form = AddWordForm()
		
	return render_to_response('word.html', {'key_word': key_word, 'form': form})

