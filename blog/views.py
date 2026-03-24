from django.shortcuts import render,redirect
from django.views import View
from blog.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    
    def post(self,request):
        name=request.POST.get('name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1!=password2 :
            return redirect('register')
        
        user=User.objects.create_user(
            username=name,
            email=email,
            password=password1,
        )
        user.save()

        return redirect('login')


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        name=request.POST.get('name')
        password=request.POST.get('password')

        user=authenticate(
            username=name,
            password=password,
        )
        if user is not None:
            login(request, user) 
            return redirect('home')
        else:
            return redirect('login')


class HomeView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('login') 
        return render(request,'home.html')
    


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')
        
    

class ArticleView(View):
    def get(self,request):
        article=Article.objects.all().order_by('-id')
        context={
            'article':article,
        }
        return render(request,'article.html' ,context)
    

class DetailsView(View):
    def get(self,request,id):
        article=Article.objects.get(id=id)
        context={
            'article':article,
        }
        return render(request,'details.html',context)
    # def post(self,request,id):
        


        # return render(request,'')


class AddView(View):
    def get(self,request):
        tags=Tag.objects.all()

        context={
            'tags':tags
        }

        return render(request,'add.html',context)
    
    def post(self,request):
        user=request.user

        title=request.POST.get('title')
        context=request.POST.get('context')
        tags=request.POST.get('tag')
        tag=Tag.objects.get(name=tags)

        article=Article.objects.create(
            title=title,
            context=context,
            author=user,
        )
        article.tags.add(tag) 

        return redirect('article')
    

class MyView(View):
    def get(self,request):
        article=Article.objects.filter(author=request.user)

        context={
            'article':article,
        }

        return render(request,'my.html',context)