from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
<<<<<<< HEAD
	return render(request, 'blog/post_list.html', {})

# Create your views here.
=======
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
    
>>>>>>> 3735a0913fd5a63f0260e469347b1303ad325daa
