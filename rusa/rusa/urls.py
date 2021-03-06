"""rusa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rusaweb.views import (
	home,
	signupForm,
	userAccount,
	listTasks,
	logoutUser,
	getTask,
	getAllUsers,
	getUser,
)
from django.contrib.auth.views import login

urlpatterns = [
	url(r'^$', home, name="home"),
	url(r'^signup/', signupForm, name="signup"),
	url(r'^login/', login, name="login"),
	url(r'^accounts/users/$', getAllUsers, name="get_users"),
	url(r'^accounts/users/(?P<user_id>[\w]+)/$', getUser, name="get_user"),
	url(r'^accounts/profile/$', userAccount, name="account"),
	url(r'^accounts/logout/$', logoutUser, name="logout"),
	url(r'^accounts/tasks/$', listTasks, name="tasks"),
	url(r'^accounts/tasks/done/$', listTasks, name="completed_tasks"),
	url(r'^accounts/tasks/(?P<task_id>[\w]+)/$', getTask, name="task_info"),
    url(r'^admin/', admin.site.urls),
]
