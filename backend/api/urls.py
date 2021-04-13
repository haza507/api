from django.urls import path, include
from django.contrib.auth.decorators import login_required
from api.views import UsuarioViewSet, GeneralesViewSet,UserViewSet,AuthViewSet
from tareas.views import TareasViewSet
from rest_framework import routers
# Django REST Framework
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

#from decorator_include import decorator_include
from api import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

router.register('generales', GeneralesViewSet)
router.register('core/user', UsuarioViewSet)
router.register('tareas', TareasViewSet)

urlpatterns = [
    #path('logout/', views.Logout.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 
    #path('', decorator_include(login_required, router.urls)),
    path('',  include(router.urls)),
]