import json

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from shop.models import Profile
from userextends.forms import UserForm, UpdateUserForm, ChangePasswordForm, UserInfoForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, 'User updated successfully!')
            return redirect('home-page')
        return render(request, 'registration/update_user.html', {'user_form': user_form})
    else:
        messages.success(request, 'You must be logged to access this page.')
        return redirect('home-page')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                login(request, current_user)
                return redirect('user-update')
            else:
                for error in list(form.errors.values()):
                    return redirect('update-password')
        else:
            messages.error(request, 'There was an error please try again.')
            form = ChangePasswordForm(current_user)
            return render(request, 'registration/update_password.html', {'form': form})

    else:
        messages.error(request, 'You must be logged in to change the password')
        return redirect('home-page')


def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()

            messages.success(request, 'User updated successfully!')
            return redirect('home-page')
        return render(request, 'registration/update_info.html', {'form': form})
    else:
        messages.success(request, 'You must be logged to access this page.')
        return redirect('home-page')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart

            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

            return redirect('home-page')
        else:
            messages.success(request, 'There was an error please try again')
            return redirect('registration/login.html')
            # return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home-page')
