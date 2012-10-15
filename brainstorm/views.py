# Create your views here.
from brainstorm.models import KeyWord
from django.shortcuts import render_to_response
from random import randint

def index(request):
	
	max_num = KeyWord.objects.all().order_by("-id")[0].id
	random_word_id = randint(1, max_num)
	random_word = KeyWord.objects.get(id=random_word_id)
	
	return render_to_response('index.html', {'random_word': random_word})