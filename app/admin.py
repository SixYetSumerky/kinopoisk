from django.contrib import admin
from app.models import *

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display=(
		'title',
		'rating',
		'release_date',
		'budget',
	)
	list_editable=(
		'budget',
	)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display=(
		'name',
	)

@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
	list_display=(
		'name',
		'role',
	)

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
	list_display=(
		'author',
		'created_at',
	)