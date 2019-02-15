# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

from utils.images import create_thumb_from_file
from .forms import PostForm, DeleteForm
from .models import Post


@login_required(login_url="/login")
def image_new(request):
    """ Page with form for image upload
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            create_thumb_from_file(post.orig_name)
            return redirect('image_detail', pk=post.id)
    else:
        form = PostForm()

    return render(request, 'imagehosting/index.html', {'form': form})


def image_detail(request, pk):
    """ Handler for page with selected image
    """
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'imagehosting/image.html', {'post': post})


def all_posts(request):
    """ Handler for main page with all images
    """
    img_list = Post.objects.order_by('-pk')
    paginator = Paginator(img_list, 50)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:  # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:  # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'imagehosting/all.html', {'all': posts})


@login_required(login_url="/login")
def delete_post(request, pk):
    """ Handler for delete page
    """
    post_to_delete = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
        form = DeleteForm(request.POST, instance=post_to_delete)
        if form.is_valid():  # checks CSRF
            post_to_delete.delete()
            return redirect('all_posts')
        # TODO: return error msg if not valid

    return render(request, 'imagehosting/delete.html', {'form': form})
