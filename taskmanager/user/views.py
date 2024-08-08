from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserUpdateSerializer, UserDeleteSerializer
from .models import User

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
