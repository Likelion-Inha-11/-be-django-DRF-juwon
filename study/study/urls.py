"""
URL configuration for study project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import * 
from post.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', Signup.as_view()),
    path('login/', Login.as_view()),
    path('myinfo/', MyInfo.as_view()),

    path('postcreate/', PostCreate.as_view()),
    path('postread/', PostRead.as_view()),
    path('postupdate/', PostUpdate.as_view()),
    path('postdelete/', PostDelete.as_view()),

    path('commentcreate/', CommentCreate.as_view()),
    path('commentread/', CommentRead.as_view()),
    path('commentupdate/', CommentUpdate.as_view()),
    path('commentdelete/', CommentDelete.as_view()),

    path('Q1/', Q1.as_view()),
    path('Q2/', Q2.as_view()),
    path('Q3/', Q3.as_view()),
    path('Q4/', Q4.as_view()),
    path('Q5/', Q5.as_view()),
    path('Q6/', Q6.as_view()),
]
