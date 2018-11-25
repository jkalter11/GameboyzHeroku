from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

app_name = 'shop'

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('Games', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('About', views.about, name='about'),
    path('Contact', views.contact, name='contact'),
    path('Reviews', views.game_reviews, name='game_reviews')



]