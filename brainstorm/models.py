from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class KeyWord(models.Model):
	
	word_name = models.CharField(max_length = 30, unique = True)
	create_date = models.DateTimeField(auto_now_add = True)
	link = models.URLField(blank = True)
	related_word = models.ManyToManyField("self", blank = True)
	creater = models.ForeignKey(User)
	
	def rel_word(self):
		return " , ".join(a.word_name for a in self.related_word.all())
		
	rel_word.short_description = "Related Word"
	
	def __unicode__(self):
		return self.word_name