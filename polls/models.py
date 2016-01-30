from django.db import models
import time

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    class Meta():
        db_table = 'question'
        
    def __str__(self):
        return self.question_text+"->%s" %self.pub_date.strftime('%Y-%m-%d %X')
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    
    class Meta():
        db_table = 'choice'
        
    def __unicode__(self):
        return self.question.question_text + "->" +self.choice_text+":%d" %self.votes