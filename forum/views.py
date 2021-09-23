from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Topic
from .forms import PostForm, CommentForm, TopicForm
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)

# Create your views here.


@login_required
def forum(response):
    if response.user.userprofile.role == "2" or response.user.userprofile.role == "1":

        form = TopicForm()
        if response.method == "POST":
            form = TopicForm(response.POST)
            form.save()
        topics = Topic.objects.filter().order_by('timestamp')

        return render(response, 'cp/forum/forum_topic.html', {
            "form": form,
            "topics": topics
        })

    else:

        topics = Topic.objects.filter().order_by('timestamp')
        return render(response, 'faculty/forum/forum_topic.html', {
            "topics": topics
        })


def discussion(response, id):
    topic = Topic.objects.filter(id=id).first()
    posts = Post.objects.filter(topic=topic)
    user = response.user


    form = PostForm()
    if response.method == "POST":
        form = PostForm(response.POST)
        if form.is_valid():
            user = response.user
            title = response.POST.get('title','')
            content = response.POST.get('post_content','')
            image = response.POST.get('image','')

            post = Post(user=user, topic=topic, title = title, post_content=content, image=image)
            post.save()
            return redirect('discussion', id)

    return render(response, 'cp/forum/forum.html',{
        "topic":topic,
        'form':form,
        'posts':posts,
        'user': user,

    })


def comments(response, id):

    post =Post.objects.filter(id=id).first()
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    user = response.user
    if response.method == "POST":
        form = CommentForm(response.POST)
        if form.is_valid():

            user = response.user
            comment = response.POST.get('comment_content','')
            image = response.POST.get('image', '')
            reply = Comment(post=post, user=user, comment_content=comment, image=image)
            reply.save()
            print("here")

    return render(response, 'cp/forum/discussion.html',{
        'post':post,
        'comments':comments,
        'form':form,
        'user':user,
    })



def update_topic(response, id):

    if id:
        topic = get_object_or_404(Topic,id=id)
    if response.method == "POST":
        form = TopicForm(response.POST, instance=topic)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('forum')
    else:
        form = TopicForm(instance=topic)

    return render(response, 'edit_topic.html',{
        'form':form
    })





def update_forum(response, id):

    if id:
        post1 = get_object_or_404(Post,id=id)
        print("here")
    if response.method == "POST":
        form = PostForm(response.POST, instance=post1)
        print("here")

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('discussion', post1.topic.id)
    else:
        form = PostForm(instance=post1)

    return render(response, 'edit_forum.html',{
        'form':form
    })


def update_reply(response, id):

    if id:
        comment = get_object_or_404(Comment,id=id)
        print("here")
    if response.method == "POST":
        form = CommentForm(response.POST, instance=comment)
        print("here")

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('discussion_info', comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(response, 'edit_reply.html',{
        'form':form
    })

