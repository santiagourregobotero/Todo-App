from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.views import View
from todoapp.forms import RegisterUser,LoginUser,TasksForm
from todoapp.models import Tasks
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json




class RegisterUserView(View):
    def post(self,request,*args,**kwargs):
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                return redirect("todo:home")
        return render(request,"register.html",{"form":form}) 
        


    def get(self,request,*args,**kwargs):
        form = RegisterUser()
        return render(request,"register.html",{"form":form})
    

class LoginUserView(View):
    def post(self,request,*args,**kwargs):
        form = LoginUser(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user=authenticate(username=username,password=password) 
            if user :
                login(request,user)
                return redirect("todo:home")
        return render(request,"login.html",{"form":form}) 
        


    def get(self,request,*args,**kwargs):
        form = LoginUser()
        return render(request,"login.html",{"form":form})  
    


class HomeView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        tasks = Tasks.objects.filter(user=request.user)
        form = TasksForm()
        context = {
            "form":form,
            "tasks":tasks
        }
        return render(request,"home.html",context=context)
    

    



class AddTaskView(View):
    def post(self,request,*args,**kwargs):
        tasks_data = json.loads(request.body)
        form = TasksForm(tasks_data)
        if form.is_valid():
            tasks = form.save(commit=False)
            tasks.user = request.user
            tasks.save()
            print(form.data)
            return JsonResponse({"data":form.data,"id":tasks.id,"is_completed":tasks.is_completed})
        return JsonResponse({"message":"fail"})


class DeleteTask(View):
    def delete(self,request,*args,**kwargs):
        task = Tasks.objects.filter(id=kwargs.get("id"))
        if not task:
            return JsonResponse({"message":"Failed"})
        task.delete()
        return JsonResponse({"message":"success","data":[]})