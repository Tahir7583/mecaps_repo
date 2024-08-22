from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views  import applicant_data

from rest_framework_simplejwt.views import (     #
    TokenObtainPairView,
    TokenRefreshView,
)


# router = DefaultRouter()
# router.register(r'skill',skillView,basename='skill')





urlpatterns = [
#    path('',include(router.urls)),
                             # applicant urls
   path('get-applicant/',applicant_data.as_view(),name='get-applicant'),
#    path('update-applicant/<int:pk>/',applicant_data.as_view(),name='update-data'),
#    path ('delete-applicant/<int:pk>/',applicant_data.as_view(),name='delete'),

   
                              # skill urls
#  






#    path('update-skill/<int:pk>/', skillView.as_view(),name='get'),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
