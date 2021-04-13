# Django
from django.contrib.auth import password_validation, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import RegexValidator, FileExtensionValidator
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from rest_framework import serializers 
from core.models import User,Generales

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','imagen','tipo','email','is_active')


class GeneralesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generales
        fields = ('id','nombre','correo','web','imagen')

#login
class UserLoginSerializer(serializers.Serializer):

    # Campos que vamos a requerir
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)

    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')
        #valores
        
        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data
 
    def create(self, data):
        """Generar o recuperar token."""
        refresh = RefreshToken.for_user(user=self.context['user'])
        token = {'refresh': str(refresh),'access': str(refresh.access_token),
            }        
        return self.context['user'], token['access']
    
  #  def create(self, data):
  #      """Generar o recuperar token."""
  #      token, created = Token.objects.get_or_create(user=self.context['user'])
  #      return self.context['user'], token.key
  #  def get_tokens_for_user(self,data):
  #      refresh = RefreshToken.for_user(user=self.context['user'])
  #      
  #      return {
  #      'refresh': str(refresh),
  #      'access': str(refresh.access_token),
  #      }
class UserLogoutSerializer(serializers.Serializer):

    # Campos que vamos a requerir
    username = serializers.CharField()
    
    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['username'])
        if not user:
            raise serializers.ValidationError('Usuario no Proporcionado')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data
##crear usuario
class UserSignUpSerializer(serializers.Serializer):

    
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

   # first_name = serializers.CharField(min_length=2, max_length=50)
   # last_name = serializers.CharField(min_length=2, max_length=100)
    
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)
    tipo= serializers.CharField(default="Estudiante")
    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)

        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user