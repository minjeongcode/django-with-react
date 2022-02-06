from django.urls import path
from blog1 import views

app_name = 'blog1' # URL Reverse에서 namespace역할을 하게 됨.

urlpatterns = [
    path('', views.post_list, name='post_list')
]