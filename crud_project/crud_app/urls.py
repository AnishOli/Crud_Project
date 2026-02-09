from django.urls import path
from .views import *
urlpatterns = [
    path('', home,name= 'home'),
    path('form/', form,name= 'form'),
    path('services/', services,name= 'services'),
    path('blog/', blog,name= 'blog'),
    path('delete/<int:id>', delete_data,name= 'delete'),
]
