from django.shortcuts import render,HttpResponse,redirect
from .models import Post,BlogComment
from django.contrib import messages

from django.http import HttpRequest  
  
def mypage(request):  
    client_address = request.META['REMOTE_ADDR']  
    print(client_address)
    return client_address

def bloghome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request,"blog/bloghome.html",context)
    
def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = BlogComment.objects.filter(post=post)
    subposts = Post.objects.filter(category=post.category)
    a=[]
    for i in subposts:
        if i.title == post.title:
            pass
        else:
            a.append(i)
    print(request.user)
    print(a)
    mypage(request)
    context = {'post': post,'subposts':a,'comments':comments}
    return render(request,"blog/blogpost.html",context)

def postComment(request):
    if request.method=="POST":
        comment = request.POST.get('comment')
        print(f"{comment} jkfhduhsuhdishid")
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        
        comment = BlogComment(comment=comment,user=user,post=post)
                 
        comment.save()
        messages.success(request,"Your Comment has been posted successfull")
    return redirect(f'/blog/{post.slug}')
