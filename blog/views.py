from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)

# def home(request):
# 	posts = Post.objects.all()
# 	context = {
# 		'posts': posts
# 	}
# 	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post

	# <app>/<model>_list.html --> template naming convention
	template_name = 'blog/home.html'
	
	# if list variable used in list template is not named 'object'(here its 'post'),
	# reset it using context_object_name
	context_object_name = 'posts'
	
	# order list using the object attribute
	ordering = ['-date_posted']
	
	# posts per page
	paginate_by = 5


class UserPostListView(ListView):
	model = Post

	# <app>/<model>_list.html --> template naming convention
	template_name = 'blog/user_post.html'
	
	# if list variable used in list template is not named 'object'(here its 'post'),
	# reset it using context_object_name
	context_object_name = 'posts'
	
	# order list using the object attribute
	# ordering = ['-date_posted']
	
	# posts per page
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	# <app>/<model>_detail.html --> template naming convention
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	# <app>/<model>_form.html --> template naming convention
	model = Post
	fields = ['title', 'content']

	# IntegrityError at /post/new/
	# null value in column "author_id" violates not-null constraint
	# no author specified for the post
	# provide author to the form instance by overriding 'form_valid()' and
	# then run 'form_valid()' with the form data
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	# <app>/<model>_form.html --> template naming convention
	model = Post
	fields = ['title', 'content']

	# IntegrityError at /post/new/
	# null value in column "author_id" violates not-null constraint
	# no author specified for the post
	# provide author to the form instance by overriding 'form_valid()' and
	# then run 'form_valid()' with the form data
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	# to ensure that only the user who created a post can update that post
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	# <app>/<model>_confirm_delete.html --> template naming convention
	model = Post

	# ImproperlyConfigured at /post/10/delete/
	# No URL to redirect to. Provide a success_url.
	success_url = '/'

	# to ensure that only the user who created a post can update that post
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
	context = {
		'title': 'About'
	}
	return render(request, 'blog/about.html', context)