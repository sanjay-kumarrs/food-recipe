from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout #fuction to authenticate the login and logout 
from django.contrib.auth.decorators import login_required,user_passes_test #used so that if we need to get to the home page we must login
from django.contrib import messages #it is used to display the messages like usernaem already exists
from modules.models import recipes
from modules.models import chef
from modules.models import UserProfile
from chef_info.models import feedBack
import requests
import json


def MyHtml(request):
    return render(request,"index.html")

#------------------------------------signup----------------------------------------------------------
def Signup(request):
    if request.method=="POST":#entering the required fields to setup signup
        uname=request.POST.get('name')
        email=request.POST.get('email')
        name=request.POST.get('username')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password2')
        user= User.objects.filter( email = email)
        if user.exists():#checking if user already exists or not
            messages.info(request, "Email already exists") #iif eexists then the message is displayed
            return redirect('signup')
        if pass1 != pass2:#checking if the password you entered is same or not
             messages.info(request, "password is not the same")#if password is not the same then the following message is displayed
             return redirect('signup')
        t=request.POST.get('terms')
        my_user = User.objects.create_user(email, name, pass1)
        user_profile = UserProfile(user=my_user, is_approved=False)
        user_profile.save()
        #my_user=User.objects.create_user(email,name,pass1) #selecting the required fields for future signins and also creaye_user oonly takes 3 input arguments
        #my_user.save()#saving the created user into the database
        return redirect('login') 
    
    
    return render(request,'register.html')
#------------------------------------------------------end signup------------------------------------------------------------

#-----------------------------------------------------login------------------------------------------------------------------
@user_passes_test(lambda u: u.is_staff)
def approve_user(request, user_id):
    user_profile = UserProfile.objects.get(user_id=user_id)
    user_profile.is_approved = True
    user_profile.save()
def logins(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        rem=request.POST.get('remember')
        user=authenticate(request,username=username,password=pass1)#checking if the users username and password are the same or not
        '''if user is not None :
            login(request,user)
            return redirect("home")
        else:
            messages.info(request, "You entered wrong credentials")
            return redirect("login")'''
        if user is not None and user.userprofile.is_approved:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Your account is not approved yet.")
            return redirect("login")

    return render(request,'login.html')


#--------------------------------------------------------------------end login------------------------------------------------

#---------------------------------------------------------------------logout--------------------------------------------------
def LogoutPage(request):
    logout(request)
    return redirect('home')
#----------------------------------------------------------------------end logout---------------------------------------------

#-------------------------------------------------------------------dispaly recipe-------------------------------------------
@login_required(login_url='login')
def addfeed(request):
    if request.method == "POST":     
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        en = feedBack(name=name,email=email,subject=subject,message=message)
        en.save()
        return redirect('home')
    return render(request,'index.html')
# Create your views here.
@login_required(login_url='login')
def food(request):
    recipeData=recipes.objects.all()
    if request.method=="GET":
        st=request.GET.get('recipe_name')
        if st!=None:
            recipeData = recipes.objects.filter(recipe_name__icontains=st)#it is used to search the recipe and icontains is used so that even if we enter one word also it will search it 
    data={
        'recipeData':recipeData
    }
    return render(request,'search.html',data)

def recipes_details(request):
    recipe_name = request.GET.get('recipe_name')
    recipe = recipes.objects.get(recipe_name=recipe_name)
    datas = {
        'recipe': recipe
    }
    return render(request, 'recipe_details.html',datas)

@login_required(login_url='login')
def chef_details(request):
    chefData = chef.objects.all()
    data={
        'chefData':chefData
    }
    return render( request , "chef_details.html",data)

@login_required(login_url='login')
def chef_info(request):
    chef_name = request.GET.get('chef_name')
    chefs = chef.objects.get(chef_name=chef_name)
    datas = {
        'chefs': chefs
    }
    return render(request, "chef_info.html",datas)

@login_required(login_url='login')
def cal(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        
        # Using the API-Ninjas key which is compatible with the nutrition fields in calorie.html
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'eU2LAFR0w76frNct1FfFVQ==c69DnUHHFtWyY3iL'})
        
        try:
            api = api_request.json()
            if not api:
                api = "oops! There was an error "
        except Exception as e:
            api = "oops! There was an error "
            print(f"Error: {e}")
            
        return render(request, 'calorie.html', {'api': api})
    else:
        return render(request, 'calorie.html', {'query': 'enter a valid query'})

@login_required(login_url='login')
def apis(request):
    """
    Calorie search using Nutrition API (GET request).
    """
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        
        # Using the API-Ninjas key
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'eU2LAFR0w76frNct1FfFVQ==c69DnUHHFtWyY3iL'})
        
        try:
            api = api_request.json()
            if not api:
                api = "oops! There was an error "
        except Exception as e:
            api = "oops! There was an error "
            print(f"Error: {e}")
            
        return render(request, 'calorie.html', {'api': api})
    else:
        return render(request, 'calorie.html', {'query': 'enter a valid query'})
    

