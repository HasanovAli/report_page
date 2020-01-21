from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView

from report.models import Entry
from .forms import LoginForm, UserRegistrationForm, UserEditForm, EntryAddForm


def readme(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully.')
                else:
                    return HttpResponse('Disabled account.')

        else:
            return HttpResponse('Invalid login or password.')

    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #  create new user but not save in db
            new_user = user_form.save(commit=False)
            #  pass to user encrypted password
            new_user.set_password(user_form.cleaned_data['password'])
            # Profile.objects.create(user=new_user)
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, 'account/edit.html', {'user_form': user_form})


@login_required
def entry_list(request, entry_id=None):

    if entry_id:
        object_list = get_object_or_404(Entry, id=entry_id)
        return render(request, 'entry/detail.html', {'entry': object_list})
    else:
        object_list = Entry.objects.filter(user=request.user)

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)
    return render(request, 'entry/list.html', {'page': page, 'entries': entries})


@login_required
def entry_create(request):
    if request.method == 'POST':
        form = EntryAddForm(data=request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, "Entry added successfully")
            return redirect(new_item.get_absolute_url())
    else:
        form = EntryAddForm(data=request.GET)
    return render(request, 'entry/create.html', {'form': form})


@login_required
def entry_remove(request, entry_id=None):
    entry = get_object_or_404(Entry, id=entry_id)
    entry.delete()
    return redirect('report:entry_list')
