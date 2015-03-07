from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post, Comment, Tag
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from blog.forms import CommentForm
import time
from calendar import month_name

# Create your views here.
def index(request):
	context_dict = {}
	context_dict['months'] = mkmonths()
	return render(request,'blog/index.html',context_dict)

def blog(request):
	post = Post.objects.all().order_by("-posted")
	comment = Comment.objects.filter(post=post).count()
	paginator = Paginator(post, 2)
	try:
		page = int(request.GET.get("page",'1'))
	except ValueError:
		page = 1

	try:
		post = paginator.page(page)
	except(InvalidPage, EmptyPage):
		post = paginator.page(paginator.num_pages)
	#category = Category.objects.all()
	context_dict = {'posts':post}
	context_dict['months'] = mkmonths()
	tag = Tag.objects.all()
	pag_cnt = post.end_index()
	context_dict['cnt'] = range(1,paginator.num_pages+1)
	context_dict['comment'] = comment
	context_dict['tag'] = tag
	return render(request,'blog/blog.html',context_dict)

def view_post(request, slug):
	post = Post.objects.get(slug=slug)
	comment = Comment.objects.filter(post=post)
	context_dict = {'post': post}
	context_dict['comments'] = comment
	context_dict['form'] = CommentForm()
	context_dict['months'] = mkmonths()
	return render(request, 'blog/view_post.html',context_dict)

def about(request):
	if request.session.get('visits'):
		count = request.session.get('visits')
	else:
		count = 0
	context_dict = {'visits' : count}
	context_dict['months'] = mkmonths()
	return render(request, 'blog/about.html',context_dict)

def add_comment(request, slug):
	p = request.POST
	context_dict = {'post' : p}
	if request.method == 'POST':
		author = "Anonymous"
		if p["author"]:
			author = p["author"]
		comment = Comment(post=Post.objects.get(slug=slug))
		cf = CommentForm(p, instance=comment)
		cf.fields["author"].required = False
		comment = cf.save(commit=False)
		comment.author = author
		comment.save()
		context_dict['months'] = mkmonths()
		return view_post(request, slug)
	return render(request, 'blog/view_post.html',context_dict)

def mkmonths():
	if not Post.objects.count():
		return []
	year, month = time.localtime()[:2]
	first = Post.objects.order_by("posted")[0]
	first_year = first.posted.year
	first_month = first.posted.month
	months = []

	for y in range(year, first_year-1,-1):
		start = 12
		end = 0
		if y == year:
			start = month
		if y == first_year:
			end = first_month-1

		for m in range(start, end, -1):
			months.append((y,m,month_name[m]))
	return months

def month(request, year, month):
	posts = Post.objects.filter(posted__year=year, posted__month=month)
	return render(request, "blog/month.html", {'posts':posts, 'months' : mkmonths()})

def view_post_by_tag(request,slug):
	tag = get_object_or_404(Tag, slug=slug)
	post = Post.objects.all().filter(tag=tag)
	context_dict = {'posts':post, 'tag':tag}
	context_dict['months'] = mkmonths()
	return render(request, "blog/tag.html", context_dict)