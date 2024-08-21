from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views  import applicant_data,skillView


router = DefaultRouter()
router.register(r'skill',skillView,basename='skill')
router.register(r'skill', skillView, basename='skill')




urlpatterns = [
   path('',include(router.urls)),
                             # applicant urls
   path('get-applicant/',applicant_data.as_view(),name='get-applicant'),
   path('update-applicant/<int:pk>/',applicant_data.as_view(),name='update-data'),
   path ('delete-applicant/<int:pk>/',applicant_data.as_view(),name='delete'),

   
                              # skill urls
   # path('get-skill/',skillView.as_view(),name='get'),
   # path('update-skill/<int:pk>/', skillView.as_view(),name='get'),
 
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
