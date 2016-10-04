from django.conf.urls import patterns, include, url
from django.contrib.auth import views
from django.contrib import admin
from myapp.forms import LoginForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
                        #url(r'^login/', 'myapp.views.login', name='login'),
                        url(r'^login/$', views.login, {'template_name': 'user/login.html', 'authentication_form': LoginForm}),
                        url(r'^registration/$', 'myapp.views.registration', name='registration'),
                        #url('^registration/', CreateView.as_view(template_name='user/registration.html', form_class=UserCreationForm, success_url='/')),
                        url(r'^home/$', 'myapp.views.home', name='home'),
                        url(r'^editprofile/$', 'myapp.views.editprofile', name='editprofile'),
                        url(r'^logout/$', views.logout, {'next_page': '/myapp/login'}),
                       )