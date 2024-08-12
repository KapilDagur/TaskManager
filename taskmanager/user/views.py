from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserUpdateSerializer, UserDeleteSerializer
from .models import User
from django.contrib.auth import authenticate, login

from .serializers import  LoginSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as auth_login
from django.core.exceptions import ObjectDoesNotExist
from .serializers import LoginSerializer
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.db.models import Q












class UserRegistrationView(APIView):
    def get(self, request):
        # Render the registration form
        return render(request, 'register.html')

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('user-register-success')
        return render(request, 'register.html', {'errors': serializer.errors})

class UserUpdateView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, user_id=user_id)
        serializer = UserUpdateSerializer(instance=user)
        return render(request, 'update.html', {'user': serializer.data})

    def post(self, request, user_id):
        user = get_object_or_404(User, user_id=user_id)
        serializer = UserUpdateSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('user-update-success')
        return render(request, 'update.html', {'errors': serializer.errors})

class UserDeleteView(APIView):
    def get(self, request, user_id):
        return render(request, 'delete.html', {'user_id': user_id})

    def post(self, request, user_id):
        serializer = UserDeleteSerializer(data={'user_id': user_id})
        if serializer.is_valid():
            try:
                User.objects.get(user_id=user_id).delete()
                return redirect('user-delete-success')
            except User.DoesNotExist:
                return render(request, 'delete.html', {'error': 'User not found.', 'user_id': user_id})
        return render(request, 'delete.html', {'errors': serializer.errors, 'user_id': user_id})



User = get_user_model()

class LoginView(APIView):
    def get(self, request):
        
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            identifier = serializer.validated_data['identifier']
            password = serializer.validated_data['password']

            
            user = None
            try:
                user = User.objects.get(
                    Q(username=identifier) | Q(email=identifier) | Q(phone_number=identifier)
                )
            except ObjectDoesNotExist:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

            
            if user.check_password(password):
                auth_login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            password = form.cleaned_data['password']

            user = authenticate(request, username=identifier, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')  
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})