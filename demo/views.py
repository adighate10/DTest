from django.http import Http404
from django.shortcuts import render

# Create your views here.
from demo.models import post


def begin(request):
    try:
        p = post.objects.all()
    except post.DoesNotExist:
        raise Http404("post does not exist")
    return render(request, 'base/Blazen/d29u17ylf1ylz9.cloudfront.net/blazen-v1.html', {'posts': p})
