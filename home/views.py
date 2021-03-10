from django.shortcuts import render,HttpResponse,redirect
from .models import Contact,Author
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from blog.models import Post

# HTML pages
def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(msg)<4:
            messages.error(request, "Please fill the form correctly :)")    
        else:
            contact = Contact(name=name,email=email,phone=phone,content=msg)
            contact.save()
            messages.success(request,'Your form has been submitted :)')
   
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    query = request.GET['query']
    if len(query)>78:
        posts = []
        
    else:
        postsTitle = Post.objects.filter(title__icontains=query)
        postContent = Post.objects.filter(content__icontains=query)
        posts = postsTitle.union(postContent)
        if posts.count() == 0:
            messages.warning(request, "No search result found. Please refine your query")
    params = {'allPosts': posts,'query':query}
    return render(request,'home/search.html', params)    
    # return HttpResponse("This is search")

def aboutauthor(request,slug):
    author = Author.objects.filter(Aname=slug)
    print(author[0])
    params = {'author':author[0]}
    return render(request,'home/aboutauthor.html',params)

# Authentication APIs
def signup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        lname = request.POST['lname']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for errorneous inputs
        if len(username)>10:
            messages.error(request, "Username must be under 10 charaters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')
        if pass1!=pass2:
            messages.error(request, "Password Shoud be same :/ ")    
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your CforCode account has been succesfully created")
        return redirect('home')
    else:
        return HttpResponse("404 Not Found")    

def login(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username = loginusername,password=loginpass)
        
        if user is not None:
            auth_login(request,user)
            messages.success(request,'successfully login')
            return redirect('home')
        else:
            messages.error(request,'Invalid Creadentials :/, Please try agin')    
            return redirect('home')

    return HttpResponse("404 - not found")

def logout(request):
    auth_logout(request)
    messages.success(request,'Successfully Logged Out')
    print("hello")
    return redirect('home')    


    