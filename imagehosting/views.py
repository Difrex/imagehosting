# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post
from .forms import PostForm, DeleteForm
from django.shortcuts import redirect
from utils import files, images
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def create_thumb_from_file(filename):
        orig_file = 'config/media/images/' + filename
        # Create thumbnail
        thumb_name = images.resize_image(orig_file, {
                                    'name': filename,
                                    'size': [300, 300],
                                    'dest': 'config/media/images/'
                                    }
                            )
        return thumb_name


@login_required(login_url="/login")
def image_new(request):
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
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'imagehosting/image.html', {'post': post})


def all_posts(request,  page='1'):
        img_list = Post.objects.order_by('-pk')
        paginator = Paginator(img_list, 50)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger: # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        except EmptyPage: # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)

        return render(request, 'imagehosting/all.html', {'all': posts})


@login_required(login_url="/login")
def delete_post(request, pk):
    post_to_delete = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        form = DeleteForm(request.POST, instance=post_to_delete)
        if form.is_valid():  # checks CSRF
            if not request.user.is_authenticated():
                return HttpResponseRedirect('/admin')
            post_to_delete.delete()
            return redirect('all_posts')
    return render(request, 'imagehosting/delete.html', {'form': form})
