from django.urls import path
from .views import *

urlpatterns = [
    path('', super, name='super'), 
    ## Crud Url
    path('createuser',CreateUser.as_view(), name='createuser'),
    path('updateuser/<id>',UpdateUser.as_view(), name='updateuser'),
    path('deleteuser/<id>',DeleteUser.as_view(), name='deleteuser'),
]