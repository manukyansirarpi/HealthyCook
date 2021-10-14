from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    # path('register/', views.RegisterView.as_view(), name='register'),
    path('register/', views.register, name='register'),
    path('recipes/', views.recipes, name='recipes'),
    path('user_login/', views.user_login, name='user_login'),
]