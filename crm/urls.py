"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet
from .views import get_user_by_id
from .views import delete_user_by_id
from .views import update_user_by_id
from .views import get_all_user
from .views import login
from .views import forgot_password



from . import views

router = routers.DefaultRouter()
router.register(r'User',UserViewSet)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('getalldatabyidtodo/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
    path('getalldatatodo/', get_all_user, name='get_all_user'),
    path('deletealldatabyidtodo/<int:user_id>/', delete_user_by_id, name='delete_user_by_id'),
    path('updatealldatabyidtodo/<int:user_id>/', update_user_by_id, name='update_user_by_id'),
    path('deletealldatabyidtodo/<int:user_id>/', views.delete_user_by_id, name='delete_user_by_id'),
    path('login/', login, name='login'),
    path('forgotpassword/', forgot_password, name='forgot_password'),
]




