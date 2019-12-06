from django.urls import path,include
from registration.api import views

""""router = routers.DefaultRouter()
router.register('users',registration_list)
"""

urlpatterns = [
    path('users_socio/',views.registration_list),
    path('users_socio/<int:pk>/',views.registration_detail),
    # path('socio_users/'.views.registration_page1_list),
    # path('socio_users_auth/',views.registration_page1_auth_user_list),
]