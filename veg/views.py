from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.list import ListView
# Create your views here.

# @login_required(login_url='/login/') # if user is not login  then redirect to login_url
# def receipes(request):
#     if request.method == 'POST':
#         data = request.POST

#         # for extract we use files method becouse it is not string 
#         img = request.FILES.get('image')

#         # grtting data from fronted 
#         name =data.get('receipes_name')
#         decription =data.get('decription')

#         Receipe.objects.create(
#             receipes_name = name,
#             decription = decription,
#             image = img
#         )
#         # after submit form it reload the page or redirect to page
#         return redirect('/receipes/')

#     all_receipes = Receipe.objects.all()
#     if request.GET.get('search'):
#         all_receipes = all_receipes.filter(receipes_name__icontains = request.GET.get('search'))
        
#         print(request.GET.get('search'))
#     return render(request , 'receipes.html', context={'receipes' : all_receipes})
 

class ReceipeView(LoginRequiredMixin,ListView):
    model = Receipe
    template_name = 'receipes.html'
    login_url = '/login/'

    def get(self, request):
        all_receipes = Receipe.objects.all()
        search_query = request.GET.get('search')
        
        if search_query:
            all_receipes = all_receipes.filter(receipes_name__icontains=search_query)
        
        return render(request, 'receipes.html', context={'receipes': all_receipes})



    def post(self , request):
        data = request.POST
        img = request.FILES.get('image')
        name =data.get('receipes_name')
        decription =data.get('decription')
        Receipe.objects.create(
            receipes_name = name,
            decription = decription,
            image = img
        )
        return redirect('receipes') 



@login_required(login_url='/login/')
def delete_rec(request , id):
    print(id)
    delete_query = Receipe.objects.get(id = id)
    delete_query.delete()
    return redirect('/receipes/')


# @login_required(login_url='/login/')
def update_rec(request, id):
    print(id)
    update_query = Receipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        
        rec_name = data.get('receipes_name')
        decription = data.get('decription')
        res_image = request.FILES.get('image')

        # Remove trailing commas to avoid storing values as tuples
        update_query.receipes_name = rec_name
        update_query.decription = decription
        if res_image:
            update_query.image = res_image
        update_query.save()

        return redirect('/receipes/')

    return render(request, 'update.html', context={'recipe': update_query})


def logout_page(request):
    logout(request)
    return redirect('/login/')

class LoginPageView(View):
    def get(self,request):
        return render(request , 'login.html')

        
    def post(self,request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password=request.POST.get('password')
            # user = User.objects.filter(username=username)

            # it is checking username is exits or not
            # if not user.exists():
            #     messages.info(request ,'Invalid Username')
            #     return redirect('/login/')

            auth_user = authenticate(username=username,password=password)
            if auth_user is None:
                messages.info(request ,'Invalid Username or Password')

            else:
                login(request,auth_user)
                return redirect('/receipes/')
                

        return render(request , 'login.html')

class RegisterView(View):
    def get(self,request):
        return render(request, 'registor.html')
        
    def post(self,request):
        if request.method == "POST":

            username = request.POST.get('username')
            password=request.POST.get('password')
            user = User.objects.filter(username=username)

            if user.exists():
                messages.info(request, "Username already exits.")
                return redirect('/registor/')

            user = User.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                username=username,
            )
            

            user.set_password(password) #hasing password it is built-in methos of djnago User model
                
            
            user.save()
            messages.info(request, "Account Created Successfully")
        return render(request , 'registor.html')
 