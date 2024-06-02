from django.shortcuts import render,redirect
from .models import *
from core.models import User
from django.contrib.auth import authenticate, login

def movieList(request):
	movies=Movie.objects.all()
	return(render(request,'app/movies/list.html',{'movies':movies}))

def movieDetail(request,movie_id):
	movie=Movie.objects.get(id=movie_id)
	reviews=MovieReview.objects.filter(movie_id=movie_id).order_by('-created_at')
	return(render(request,'app/movies/detail.html',{'movie':movie,'reviews':reviews}))


def genreList(request):
	genres=Genre.objects.all()
	return(render(request,'app/genre/list.html',{'genres':genres}))

def genreDetail(request,genre_id):
	genre=Genre.objects.get(id=genre_id)
	return(render(request,'app/genre/detail.html',{'genre':genre}))


def personsList(request,person_role):
	persons=MoviePerson.objects.filter(role=person_role)
	if(person_role==MoviePerson.RoleType.ACTOR):
		title='Актёры'
	else:
		title='Режисёры'
	return(render(request,'app/person/list.html',{'persons':persons,'title':title}))


def personDetail(request,person_id):
	person=MoviePerson.objects.get(id=person_id)
	if(person.role==MoviePerson.RoleType.ACTOR):
		movies=person.acted_in_movies.all()
	else:
		movies=person.directed_movies.all()
	return(render(request,'app/person/detail.html'),{'person':person,'movies':movies})


def home(request):
	movies=Movie.objects.all()
	return(render(request,'app/home.html',{'movies': movies}))

def reg(request):
	if(request.user.is_authenticated):
		return(redirect('home'))
	if(request.method=='POST'):
		login=request.POST['login']
		password=request.POST['password']
		repeatpassword=request.POST['repeatpassword']
		email=request.POST['email']
		if(repeatpassword!=password):
			return(render(request,'app/profile/reg.html',{'error':1,'login':login,'email':email}))
		User.objects.create_user(
			username=login,
			email=email,
			password=password,
		)
		return(redirect('home'))
	return(render(request,'app/profile/reg.html',{'error':0}))

def log(request):
	if(request.user.is_authenticated):
		return(redirect('home'))
	if(request.method=='POST'):
		logusername=request.POST['login']
		logpassword=request.POST['password']
		user=authenticate(request,username=logusername,password=logpassword)
		if(user is not None):
			login(request,user)
			return(redirect('home'))
		return(render(request,'app/profile/log.html',{'error':2,'logusername':logusername}))
	return(render(request,'app/profile/log.html',{'error':0,}))

def profile(request):
	if(not(request.user.is_authenticated)):
		return(redirect('home'))
	return(render(request,'app/profile/profile.html'))

def logout(request):
	from django.contrib.auth import logout
	logout(request)
	return(redirect('home'))

def addreview(request):
	if(not(request.user.is_authenticated)):
		return(redirect('home'))
	print(request.POST)
	if(request.method=='POST'):
		movieid=request.POST['movieid']
		MovieReview.objects.create(
			author=request.user,
			movie=Movie.objects.get(id=movieid),
			text=request.POST['review'],
		)
		return(redirect('moviedetail',movie_id=movieid))
	return(redirect('home'))

def profileedit(request):
	if(not(request.user.is_authenticated)):
		return(redirect('home'))
	if(request.method=='POST'):
		newfirstname=request.POST['first_name']
		newemail=request.POST['email']
		icon=request.POST['icon']
		# newpassword=request.POST['password']
		# repeatpassword=request.POST['repeatpassword']
		# password=''
		# if(not newpassword==''):
		# 	if(newpassword==repeatpassword):
		# 		password=newpassword
		# 	else:
		# 		return(render(request,'app/profile/edit.html',{'passerror':1}))
		if(not(newfirstname=='')):
			request.user.first_name=newfirstname
		if(not(newemail=='')):
			request.user.email=newemail
		# if(not(icon==None)):
		# 	request.user.avatar.url=icon
		# if(not(password=='')):
		# 	request.user.password=password
		request.user.save()
		return(redirect('profile'))
	return(render(request,'app/profile/edit.html',{'error':False}))