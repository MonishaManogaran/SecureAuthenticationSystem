from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_view(request):
    error=None
    if request.method=='POST':
        email=request.POST.get('email','').strip()
        firstname=request.POST.get('firstname','').strip()
        lastname=request.POST.get('lastname','').strip()
        phonenumber=request.POST.get('phonenumber','').strip()
        password=request.POST.get('password','').strip()

        
        if not all([email, firstname, lastname, password, phonenumber]):
            error='*All fields are required'
            return render(request, 'signup.html',{
                'error':error,
                'email':email,
                'firstname':firstname,
                'lastname':lastname,
                'phonenumber':phonenumber,

            })
        
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'signup.html', {
                'error':'email is already exists',
                'email':email,
                'firstname':firstname,
                'lastname':lastname,
                'phonenumber':phonenumber,})

        try:
            CustomUser.objects.create_user(
                email=email,
                firstname=firstname,
                lastname=lastname,
                phonenumber=phonenumber,
                password=password
            )
            return redirect('login')
        except Exception:
            return render(request, 'signup.html',{
                'error':error,
                'email':email,
                'firstname':firstname,
                'lastname':lastname,
                'phonenumber':phonenumber,


            })
    return render(request, 'signup.html')

def login_view(request):
    
    if request.method=='POST':
        email=request.POST.get('email','').strip()
        password=request.POST.get('password','').strip()
        

        if email and password:
            user=authenticate(request, username=email, password=password) # tells django to check email as username
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return render(request, 'login.html',{'error':'*Invalid Credentials'})
        elif not all([email, password]):
                return render(request, 'login.html',{'error':'*Please enter email and password'})
        
    return render(request, 'login.html')


@login_required(login_url='login')
def home(request):
    firstname=request.user.firstname
    return render(request, 'index.html', {'firstname':firstname})

# api view
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import ResgisterSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterAPI(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=ResgisterSerializer
    permission_classes=[permissions.AllowAny]

class HomeAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        user=user.request
        return Response({
            'email':user.email,
            'firstname':user.firstname,
            'lastname':user.lastname,
            'phonenumber':user.phonenumber
        })
