from django import views
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm, RegistrationForm
from .mixins import CartMixin
from .models import Artist, Album, Customer


class BaseView(views.View):
    """Базовое представление"""

    def get(self, request, *args, **kwargs):
        return render(request, "base.html", {})


class ArtistDetailView(views.generic.DetailView):
    """Детализированное представление исполнителя"""

    model = Artist
    template_name = 'artist/artist_detail.html'
    slug_url_kwarg = 'artist_slug'
    context_object_name = 'artist'


class AlbumDetailView(views.generic.DetailView):
    """Детализированное представление исполнителя"""

    model = Album
    template_name = 'album/artist_detail.html'
    slug_url_kwarg = 'album_slug'
    context_object_name = 'album'


class LoginView(views.View):
    """Представление формы для авторизации"""

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'login.html', context)


class RegistrationView(views.View):
    """Представление формы для регистрации"""

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Customer.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
            )
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'registration.html', context)


class AccountView(CartMixin, views.View):
    """Представление аккаунта покупателя"""
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user = request.user)
        context = {
            'customer': customer,
            'cart': self.cart
        }
        return render(request, 'account.html', context)
