from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views  import skill_data,applicant_data

urlpatterns = [
   
   path('get/', skill_data.as_view(),name='get'),
   path('update/<int:pk>/', skill_data.as_view(),name='get'),

                  # applicant urls
   path('get-applicant/',applicant_data.as_view(),name='get-applicant'),
   path('update-applicant/<int:pk>/',applicant_data.as_view(),name='update-data'),
   path ('delete-applicant/<int:pk>/',applicant_data.as_view(),name='delete'),

  
   
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
