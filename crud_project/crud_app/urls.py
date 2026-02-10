from django.urls import path
from .views import *
urlpatterns = [
    path('', home,name= 'home'),
    path('form/', form,name= 'form'),
    path('services/', services,name= 'services'),
    path('blog/', blog,name= 'blog'),
    path('delete/<int:id>', delete_data,name= 'delete'),
    path('update/<int:id>', update_data,name= 'update'),
    path('recycle/', recycle,name= 'recycle'),
    path('restore/<int:id>', restore_data,name= 'restore'),
    path('counter/', counter,name= 'counter'),
]
