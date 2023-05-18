from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

from rest_framework import viewsets
from stats_app.models import Battle, Country, Competition, Season, Group, Freestyler
from .serializers import BattleSerializer, CountrySerializer, CompetitionSerializer, SeasonSerializer, GroupSerializer, FreestylerSerializer, TokenSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.views import APIView

# Autentication

@api_view(['POST'])
def signup(request): #Hace la llamada con Json
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)


class Login(ObtainAuthToken): #Hace la llamada con Json
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if login_serializer.is_valid():
            print("Valido")
            user = login_serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status = status.HTTP_201_CREATED)

            # Para que en cada nuevo inicio se cree un nuevo token
            # if created:
            #     return Response({"token": token.key}, status = status.HTTP_201_CREATED)
            # else:
            #     token.delete()
            #     token = Token.objects.create(user=user) 
            #     return Response({"token": token.key}, status = status.HTTP_201_CREATED)

        return Response({"message": "Username or password incorrect"}, status = status.HTTP_400_BAD_REQUEST)

class Logout(APIView): # Hace la llamada con querys
    def post(self, request, *args, **kwargs):

        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            #user = token.user
            token.delete()

            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        
        return  Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")


# Resto de Vistas

class TokenViewSet(viewsets.ModelViewSet):

    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CompetitionViewSet(viewsets.ModelViewSet):

    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

class SeasonViewSet(viewsets.ModelViewSet):

    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BattleViewSet(viewsets.ModelViewSet):

    queryset = Battle.objects.all()
    serializer_class = BattleSerializer

class FreestylerViewSet(viewsets.ModelViewSet):

    queryset = Freestyler.objects.all()
    serializer_class = FreestylerSerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer