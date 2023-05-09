from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import hikerForm
from .forms import blogForm

from .models import blog

def index(request):
    return render(request, 'index.html')

def list(request):
    blog_list = blog.objects.filter(deleted='N').order_by('-postDate')
    context = {'blog_list': blog_list}
    return render(request, 'blog/list.html', context)

def create(request):
    if request.method == 'POST':
        form = blogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.deleted = 'N'
            post.save()
            return redirect('list')
    else:
        form = blogForm()
    return render(request, 'blog/create.html', {'form': form})

def detail(request, id):
    post = get_object_or_404(blog, id=id, deleted='N')
    return render(request, 'blog/detail.html', {'post': post})

def update(request, id):
    post = get_object_or_404(blog, id=id, deleted='N')
    if request.method == 'POST':
        form = blogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', id=post.id)
    else:
        form = blogForm(instance=post)
    return render(request, 'blog/create.html', {'form': form})

def delete(request, id):
    post = get_object_or_404(blog, id=id, deleted='N')
    post.deleted = 'Y'
    post.save()
    return redirect('list')


