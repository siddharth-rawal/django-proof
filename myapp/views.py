from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from forms import RegistrationForm, UpdateUserModelFields, UpdateUserProfileModelFields
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.models import User
from myapp.models import UserProfile
import pdb

#def login(request):
    # if this is a POST request we need to process the form data
    #if request.method == 'POST':
        # create a form instance and populate it with data from the request:
      #  form = LoginForm(request.POST)

        # check whether it's valid:
      #  if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

        #    form.save()

            # success message
        #    messages.info(request, 'Domain added successfully')
          #  return HttpResponseRedirect('/polls/domainlist/')

    # if a GET (or any other method) we'll create a blank form
    #else:
     #   form = LoginForm()
    #return render(request, 'user/login.html', {'form': form})


@login_required(login_url="/myapp/login/")
def home(request):
    return render(request,"user/home.html")

@login_required(login_url="/myapp/login/")
def editprofile(request):
    user_t = get_object_or_404(User, id=request.user.id)
    try:
        userprofile_t = get_object_or_404(UserProfile, id=request.user.userprofile.id)
    except:
        userprofile_t = UserProfile()

    form1 = UpdateUserModelFields(request.POST or None, instance=user_t)
    try:
        form2 = UpdateUserProfileModelFields(instance=userprofile_t)
    except:
        form2 = UpdateUserProfileModelFields()

    if request.method == 'POST':
        form1 = UpdateUserModelFields(request.POST or None, instance=user_t)
        try:
            form2 = UpdateUserProfileModelFields(request.POST or None, request.FILES, instance=userprofile_t)
        except:
            form2 = UpdateUserProfileModelFields()
        if form1.is_valid() and form2.is_valid():
            form1.save()
            new_entry = form2.save(commit=False)
            new_entry.user = request.user
            new_entry.save()
            # success message
            messages.success(request, 'Profile updated successfully')
            # Save was successful, so redirect to another page
            return HttpResponseRedirect('/myapp/editprofile/')

    return render(request,"user/editprofile.html", {'form1' : form1, 'form2' : form2})


def registration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/myapp/home')
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    # 2nd time around
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                last_name=form.cleaned_data['last_name'],
                first_name=form.cleaned_data['first_name'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            #form.save()
            return HttpResponseRedirect('/myapp/login')

    # form with no input

    # pdb.set_trace()
    #return render(request, 'user/registration.html', {'form' : form})
    return render(request, 'user/registration.html', args)

