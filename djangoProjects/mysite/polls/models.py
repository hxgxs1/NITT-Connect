from django.db import models

# Create your models here.

class Poll(models.Model):
	question=models.CharField(max_length=100)
	pub_date=models.DateTimeField('Published Date::')
	
	def __unicode__(self):
		return self.question

	def display(self):
		print self.question,self.pub_date
	
	
class Choice(models.Model):
	poll=models.ForeignKey(Poll)
	choice_text=models.CharField(max_length=120)
	votes=models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text


# this table is for admin posts
class AdminPosts(models.Model):
	subject=models.CharField(max_length=200)
	post=models.TextField(max_length=500)
	pub_date=models.DateTimeField('Published Date::')

	def display(self):
		print self.subject, self.pub_date

	def __unicode__(self):
		return self.subject

class UserPosts(models.Model):
	subject=models.CharField(max_length=150)
	post=models.TextField(max_length=500)
	pub_date=models.DateField('Published Date')
	user_id=models.IntegerField(default=0)
	username=models.TextField(max_length=100)

		
	def __unicode__(self):
		print self.subject
	

















