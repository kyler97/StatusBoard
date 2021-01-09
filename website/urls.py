from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home' ),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
    path('unitBoard/', views.unitBoard, name='unitBoard'),
    path('inservice/<list_id>', views.inservice, name='inservice'),
    path('outofservice/<list_id>', views.outofservice, name='outofservice'),
    path('weather/', views.weather, name='weather'),
    path('station1/', views.station1, name='station1'),
    path('st2/', views.st2, name='st2'),
    path('st3/', views.st3, name='st3'),
    path('st4/', views.st4, name='st4'),
    path('addunit/', views.addunit, name='addunit'),
    path('allunits/', views.allunits, name='allunits'),
    path('editunit/<str:pk>/', views.editunit, name='editunit'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('calendar/', views.calendar, name='calendar'),

    


    
]