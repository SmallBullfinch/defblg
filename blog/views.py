from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
<<<<<<< HEAD
	return render(request, 'blog/post_list.html', {})

# Create your views here.
=======
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
<<<<<<< HEAD
def post_detail(request, pk):
	post=get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})
=======
    
>>>>>>> 3735a0913fd5a63f0260e469347b1303ad325daa
>>>>>>> 0909150ee4c237408cf7326a1b5aeb0018e40e18
