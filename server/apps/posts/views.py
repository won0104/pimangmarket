from django.shortcuts import render, redirect
from server.apps.posts.models import Post
from django.http.request import HttpRequest

def posts_list(request:HttpRequest, *args, **kwargs):
    posts = Post.objects.all()
    # text = request.GET.get("text")
    # if text:
    #     posts = posts.filter(content__contains=text)
    min_price= request.GET.get("min_price")
    max_price= request.GET.get("max_price")
        
    sort_option = request.GET.get("sort")

    context={
        "posts":posts,

    }
    if min_price and max_price:
        posts=posts.filter(price__range=(min_price,max_price))
        

    return render(request, "posts/posts_list.html", context=context)

def posts_retrieve(request:HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    user=post.user
    # all_post=user.post_set.all()
    all_post=user.post_user.all()

    user_name=post.user.name
    user_age=post.user.age
    context={
        "post": post,
        "user_name":user_name,
        "user_age": user_age,
        "all_post" : all_post,
    }
    return render(request, "posts/posts_retrieve.html", context=context)

def posts_create(request:HttpRequest, *args, **kwargs):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            user=request.POST["user"],
            region=request.POST["region"],
            price=request.POST["price"],
            content=request.POST["content"],
            photo=request.FILES["photo"],
        )
        return redirect("/")
    return render(request, "posts/posts_create.html")

def posts_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")

def posts_update(request:HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.title=request.POST["title"]
        post.user=request.POST["user"]
        post.region=request.POST["region"]
        post.price=request.POST["price"]
        post.content=request.POST["content"]
        post.photo=request.FILES["photo"],
        post.save()
        return redirect(f"/posts/{post.id}")
    return render(request, "posts/posts_update.html", {"post":post})