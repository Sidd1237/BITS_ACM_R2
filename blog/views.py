from django.shortcuts import render

posts = [
	{
		'author': 'Sidd1237',
		'title': 'Blog Post 1',
		'content': 'This is the content in post 1.',
		'date_posted': 'December 9, 2022'
	},

	{
		'author': 'Google the dog',
		'title': 'Blog Post 2',
		'content': 'This is the content in post 2.',
		'date_posted': 'December 10, 2022'
	}
]

def home(request):
	context={
			'posts':posts
		}
	return render(request, 'blog/home.html',context)

def about(request):
	return render(request,'blog/about.html',{'title':'About'})

