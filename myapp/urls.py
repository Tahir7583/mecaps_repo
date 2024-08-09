from django.urls import path
from .views  import skill_data

urlpatterns = [
   path('get/', skill_data.as_view(),name='get'),
   
   path('update/<int:pk>/', skill_data.as_view(),name='get'),
   
   
]
