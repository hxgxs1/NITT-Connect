# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from polls.models import Poll,Choice,AdminPosts
from django.template import RequestContext, loader
from django.contrib import auth
from django.core.context_processors import csrf
#from forms import MyRegForm
from django.contrib.auth.forms import UserCreationForm
from forms import userPostForm
from django.utils import timezone
from models import UserPosts
from django.contrib.auth.models import User

def index(request):

	#latest_poll_list=Poll.objects.order_by('-pub_date')[:4]
	#output=';;'.join([ p.question for p in latest_poll_list])
	#template=loader.get_template('polls/index.html')
	#context=RequestContext(request,{})
	#return HttpResponse(template.render(context))
	
	
	c={}
	c.update(csrf(request))
	# following code would reverse the posts sent by admin
	posts_list=list()
	allPosts=AdminPosts.objects.all()
	for posts in allPosts:
		posts_list.append(posts)
	
	posts_list.reverse()
	tempDict={'adminPosts':posts_list}
	c.update(tempDict)
	
	#code to get all user posts
	upostList=list()
	userposts=UserPosts.objects.all()
	for posts in userposts:
		upostList.append(posts)

	upostList.reverse()
	#print upostList[0].subject
	tempDict2={'userPosts':upostList[:3]}
	c.update(tempDict2)
	

	return render_to_response('polls/index.html',c)



def contactUs(request):
	template=loader.get_template('polls/contactus.html')
	context=RequestContext(request,{})
	return HttpResponse(template.render(context))


def auth_view(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user=auth.authenticate(username=username,password=password)
	
	if user is not None:

		user.backend = 'django.contrib.auth.backends.ModelBackend'
		auth.login(request,user)
		#template=loader.get_template('polls/home.html')
		#context=RequestContext(request,{})
		#return HttpResponse(template.render(context))
		return HttpResponseRedirect('logged/home')
	else:
		return HttpResponse('Invalid credentials')


def atHome(request):
	# for admin posts
	posts_list=list()
	allPosts=AdminPosts.objects.all()
	for posts in allPosts:
		posts_list.append(posts)
	
	posts_list.reverse();
	# for user posts
	upostList=list()
	userposts=UserPosts.objects.all()
	for posts in userposts:
		upostList.append(posts)

	upostList.reverse()

	return render_to_response('polls/logged/home.html',{'adminPosts':posts_list,'user':request.user,'userPosts':upostList[:3]})


def user_register(request):
	if request.method == 'POST':
		form=UserCreationForm(request.POST)
				
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('reg_success')

	args={}
	args.update(csrf(request))	
	args['form']=UserCreationForm()
	return render_to_response('polls/registrationForm.html',args)

	

def reg_success(request):
	return render_to_response('polls/reg_success.html')

def logout(request):
	auth.logout(request)
	return render_to_response('polls/logged/logout.html')


def userPost(request,user_id=0):
	if request.POST:
		
		form=userPostForm(request.POST)
		print user_id
		sub=request.POST.get("subject","")
		print sub
		if form.is_valid():
			form.save()
			#print 'yeah the form is valid'
			
			a=UserPosts.objects.get(subject=sub)
			a.user_id=user_id
			user=User.objects.get(id=user_id)
			a.username=user.username
			a.save()
			return HttpResponseRedirect('/polls/auth/logged/home')

		else:
			print 'form is invalid'

	args={}
	print user_id
	args.update(csrf(request))
	args['form']=userPostForm()
	args['user_id']=user_id
	return render_to_response('polls/logged/userPost.html',args)





def singlePost(request,post_id=0):
	args={}	
	post=UserPosts.objects.get(id=post_id)
	args['post']=post
	return render_to_response('polls/logged/singlePost.html',args)



def details(request, poll_id):
	return HttpResponse("You are looking for %s" % poll_id)

def result(result, poll_id):
	return HttpResponse("You are looking at the result of poll %s" % poll_id)

def vote(request, poll_id):
	return HttpResponse("You are voting on poll %s" % poll_id);
