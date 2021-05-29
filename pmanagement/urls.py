from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('commoninfo/',views.commoninfo, name='commoninfo'),
    path('commoninfo/add/',views.add, name='add'),
    path('commoninfo/fetch/',views.fetch, name='fetch'),
    path('commoninfo/list/',views.user_list, name='user_list')
]