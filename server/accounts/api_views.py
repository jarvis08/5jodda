from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm


# Create your views here.
@api_view(['GET'])
def user_detail(request, user_pk):
    User = get_user_model()
    now_user = User.objects.get(pk=user_pk)
    
    if request.method == 'GET':
        serializer = AuthenticationForm(now_user)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass
    return Response(status=405)
 

@require_POST
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return Response({'massage': 'complete'})