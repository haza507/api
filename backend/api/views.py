from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from api.serializers import UserSignUpSerializer, UserLogoutSerializer, UserModelSerializer,GeneralesSerializer,UserLoginSerializer
from rest_framework.views import APIView
from rest_framework import viewsets,status,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie
#from core.views import valid_uuid
#from rest_framework.permissions import AllowAny,IsAuthenticated
from core.models import User,Generales

class GeneralesViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication,]
    queryset = Generales.objects.all()
    serializer_class = GeneralesSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
#    authentication_classes = (TokenAuthentication, )
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


#Login
class UserViewSet(viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
 
    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
    
    

    @action(detail=False, methods=['post'])
    def logout(self, request):
        request.user.auth_token.delete()
        data = {'mensaje':'Sesión Finalizada'}
        return Response(data,status=status.HTTP_200_OK)

   

   
        
#Logout
class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserLogoutSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    
    @action(detail=False, methods=['post'])
    def logout(self, request):
        serializer = UserLogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(request.user)
        request.user.auth_token.delete()
        data = {'mensaje':'Sesión Finalizada'}
        return Response(data,status=status.HTTP_200_OK)


        #@method_decorator(csrf_protect)
        #@method_decorator(never_cache)
        #@ensure_csrf_cookie