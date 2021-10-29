from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from boards.models import BlogPost
from django.utils import timezone


# Create your views here.

# registration
def registration(request):
    if request.method =="POST":
        # checking if user with the given username already exists 
        if User.objects.filter(username=request.POST.get('uname')).exists():
            messages.error(request,"Usename already exists!",extra_tags="danger")
            return render(request,"register.html")
        # else create a user with the given username
        newUser = User.objects.create_user(
            password=request.POST.get("password"),
            last_login=timezone.now(),
            username=request.POST.get("uname"),
            first_name=request.POST.get("fname"),
            last_name=request.POST.get("lname"),
            email=request.POST.get("email"),
            date_joined=timezone.now()
        )
        newUser.save()
        messages.success(request,"Your registration was successful!",extra_tags="success")
        return redirect("/loginuser")
    else:
        return render(request,"register.html")

#login
def loginuser(request):
    if request.method == "POST":
        # checking if user with the given username exists 
        if User.objects.filter(username=request.POST.get("uname")).exists():
            user =  authenticate(username=request.POST.get("uname"),password=request.POST.get("password"))
            if user is not None:
                login(request,user)
                return redirect("/myblog")
            else:
                messages.error(request,"Incorrect Username or Password!",extra_tags="danger")
        else:
            messages.warning(request,"User with username '"+request.POST.get("uname")+"' does not exist!",extra_tags="warning")
    return render(request,"login.html")

#logout
def logoutuser(request):
    logout(request)
    return redirect("/")

#home 
def home(request):
    blogs = BlogPost.objects.all()
    if request.user.is_authenticated:
        fullname = request.user.first_name+" "+request.user.last_name
    else:
        fullname = ""
    args = {"blogs":blogs,"authenticated":request.user.is_authenticated,"fullname":fullname}
    return render(request,"index.html",args)

#myblogs
def myblog(request):
    # checking if the user is authenticated
    if request.user.is_authenticated:
        fullname = request.user.first_name+" "+request.user.last_name
        blogs = BlogPost.objects.filter(username=request.user)
        if request.method == "POST":
            # checking if the request is to delete
            if request.POST.get("blogtodelete"):
                blogtodelete = BlogPost.objects.filter(id=request.POST.get("blogtodelete"))
                messages.success(request,"'"+blogtodelete[0].title+"' was deleted successfully.")
                blogtodelete.delete()
            else:
                # checking if the request is to edit
                blogIdToEdit = request.POST.get("blogtoedit")
                if BlogPost.objects.filter(id=blogIdToEdit,username=request.user).exists():
                    editedBlog = BlogPost.objects.filter(id=blogIdToEdit,username=request.user)
                    editedBlog.update(title = request.POST.get("title"),body = request.POST.get("blogbody"),timestamp = timezone.now()) 
                    messages.success(request,"Your blog was edited successfully.")
                else:
                    newblog = BlogPost(
                        title=request.POST.get("title"),
                        body=request.POST.get("blogbody"),
                        timestamp=timezone.now(),
                        username=request.user
                    )
                    newblog.save()
                    messages.success(request,"Your blog was posted successfully.")
        args = {"blogs":blogs,"fullname":fullname}
        return render(request,"myblogs.html",args)
    else:
        return redirect("/loginuser")
        
