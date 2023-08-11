from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Titi',views.Titi, name='Titi'),
    path('product',views.product,name ='product'),
    path('blog/<int:articleid>',views.blogarticle,name= 'blogarticle'),
    path('About',views.About,name="about_website")
]
