from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class problem(models.Model):
	problem_id=models.IntegerField(max_length=10,primary_key=True) 	
	title=models.CharField(max_length=50)
	description=models.TextField()
	input=models.TextField()
	output=models.TextField()
	sample_input=models.TextField()
	sample_output=models.TextField()
	spj=models.IntegerField(max_length=2)
	hint=models.TextField(blank=True)
	source=models.CharField(max_length=100,blank=True)
	in_date=models.DateTimeField()
	time_limit=models.IntegerField(max_length=1)
	memory_limit=models.IntegerField(max_length=1)
	defunct=models.CharField(max_length=1)
	accepted=models.IntegerField(max_length=1)
	submit=models.IntegerField(max_length=1)
	solved=models.IntegerField(max_length=1)
	mark=models.IntegerField(default=5)
	diff=models.IntegerField(default=2)
	def  __unicode__(self):
		return u"%s %s" % (self.title,self.description)
		# return must unicode rather than int 



class users(models.Model):
	user=models.ForeignKey(User, unique=True)
	submit=models.IntegerField(default=0)
	solved=models.IntegerField(default=0)
	team=models.IntegerField(default=1,max_length=2)
	nickname=models.CharField(max_length=32)
	motto=models.CharField(max_length=300)
	realname=models.CharField(max_length=12)
	studentid=models.CharField(max_length=12)
	score1=models.IntegerField(default=5)
	def __unicode__(self):
		return self.user
	
class contest(models.Model):
	contest_id=models.IntegerField(primary_key=True)
	title=models.CharField(max_length=100)
	start_time=models.DateTimeField()
	end_time=models.DateTimeField()
	defunct=models.CharField(max_length=1)
	description=models.TextField()
	private=models.IntegerField()
	langmask=models.IntegerField(max_length=11)
	def __unicode__(self):
		return self.title
class contest_problem(models.Model):
	problem_id=models.IntegerField(max_length=11)
	contest_id=models.IntegerField(max_length=11)
	title=models.CharField(max_length=200,blank=True)
	num=models.IntegerField(max_length=11)
	def __unicode__(self):
		return self.title

class Contestant(models.Model):
    contest = models.ForeignKey(contest)
    user = models.ForeignKey(User)
    jointime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

class solution(models.Model):
	solution_id=models.IntegerField(max_length=10,primary_key=True)
	problem_id=models.IntegerField(max_length=10)
	user_id=models.CharField(max_length=48)
	time=models.IntegerField(max_length=11)
	memory=models.IntegerField(max_length=11)
	in_date=models.DateTimeField()
	result=models.SmallIntegerField(max_length=6)
	language=models.IntegerField(max_length=10)
	ip=models.CharField(max_length=10)
	contest_id=models.CharField(max_length=11)
	valid=models.IntegerField(max_length=4)
	num=models.IntegerField(max_length=4)
	code_length=models.IntegerField(max_length=11)
	judgetime=models.DateTimeField()
	pass_rate=models.FloatField()
	def contest_time(self):
		import contest
		if(self.in_date<=contest.self.contest_id):
			pass
	def __unicode__(self):
		return str(self.solution_id)

class source_code(models.Model):
	solution_id=models.IntegerField(primary_key=True)
	source=models.CharField(max_length=10240)
	def __unicode__(self):
		return str(self.solution_id)

class article(models.Model):
	article_id=models.IntegerField(primary_key=True)
	title=models.CharField(max_length=50)
	content=models.CharField(max_length=10240)
	time=models.DateTimeField()
	clicked=models.IntegerField(default=0)
	user_id=models.ForeignKey(User)
	parent_id=models.IntegerField(blank=True)
	variety=models.IntegerField(default=0)
	def __unicode__(self):
		return self.article_id
	
class message(models.Model):
	sender=models.CharField(max_length=50)
	receiver=models.CharField(max_length=50)
	title=models.CharField(max_length=50)
	content=models.CharField(max_length=10240)
	time=models.DateTimeField()
	def __unicode__(self):
		return self.title

class compileinfo(models.Model):
	solution_id=models.IntegerField(primary_key=True)
	error=models.CharField(max_length=1024)
	def __unicode__(self):
		return self.solution_id
		
class runtimeinfo(models.Model):
	solution_id=models.IntegerField(primary_key=True)
	error=models.CharField(max_length=1024)
	def __unicode__(self):
		return self.solution_id