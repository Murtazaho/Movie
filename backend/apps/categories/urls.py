
from django.urls import path
from .views import getCategory

urlpatterns = [
    
    
       path('', getCategory.as_view())
  
]
