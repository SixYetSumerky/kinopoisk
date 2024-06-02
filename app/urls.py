from django.urls import path
from app.views import *

urlpatterns = [
	path('',home,name='home'),
	path('movielist/',movieList,name='movielist'),
	path('moviedetail/<int:movie_id>/',movieDetail,name='moviedetail'),
	path('genrelist/',genreList,name='genrelist'),
	path('genredetail/<int:genre_id>/',genreDetail,name='genredetail'),
	path('personlist/<str:person_role>/',personsList,name='personlist'),
	path('person/<int:person_id>/',personDetail,name='persondetail'),
	path('reg/',reg,name='reg'),
	path('log/',log,name='log'),
	path('profile/',profile,name='profile'),
	path('profileedit/',profileedit,name='profileedit'),
	path('logout/',logout,name='logout'),
	path('addmoviereview/',addreview,name='addmoviereview')
]