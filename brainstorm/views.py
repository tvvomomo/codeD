# Create your views here.
from brainstorm.models import KeyWord
from django.shortcuts import render_to_response
from random import randint

def index(request):
	total_words = KeyWord.objects.all().count()
	max_num = KeyWord.objects.all().order_by("-id")[0].id
	random_word_id = randint(1, max_num)
	random_word = KeyWord.objects.get(id=random_word_id)
	return render_to_response('index.html', {'random_word': random_word, 'total_words':total_words})
	
def showWord(request, key_word_id):
	key_word = KeyWord.objects.get(id=int(key_word_id))
	return render_to_response('word.html', {'key_word': key_word})



'''
add apple to python's related_word:

python = KeyWord.objects.get(word_name='Python')
apple = KeyWord.objects.get(word_name='apple')

python.related_word.add(apple)

'''

