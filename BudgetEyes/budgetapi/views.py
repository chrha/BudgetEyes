from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate,login
from django.db import IntegrityError, OperationalError
from django.conf import settings
from django.http import FileResponse

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token

from .models import Budget, Stock, Profile
from .serializers import BudgetSerializer, StockSerializer, UserSerializer, ProfileSerializer
from .viewsets import CreateListUpdateViewSet

# Create your views here.
"""

class StockList(generics.ListCreateAPIView):
  queryset = Stock.objects.all()
  serializer_class = StockSerializer


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Stock.objects.all()
  serializer_class = StockSerializer


class OwnBudget(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = BudgetSerializer

  def get_queryset(self):
    user = self.request.user 
    return Budget.objects.filter(owner=user)
        

class UserDetail(generics.RetrieveUpdateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
"""

class UserViewSet(CreateListUpdateViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get_permissions(self):
    action = self.action
    if action == 'list':
      permission_classes = [IsAdminUser]
    elif action == 'login' or action == 'register':
      permission_classes = []
    else:
      permission_classes = [IsAuthenticated]
      
    return [permission() for permission in permission_classes]
    

  # ADD NEW ROUTES(actions) TO /auth/ HERE
   
  @action(detail=False, methods=['put'])
  def change_password(self, request):
    pw = request.data.get('new_password')
    if pw != request.data.get('new_password_re'):
      return Response("The passwords you've entered do not match", status=status.HTTP_400_BAD_REQUEST)
    token = request.headers.get('Authorization').split(' ')[1]
    user = Token.objects.select_related('user').get(key=token).user
    auth = user.check_password(pw)
    if not auth:
      user.set_password(pw)
      user.save()
      return Response(status=status.HTTP_202_ACCEPTED)
    else:
      return Response("You can't enter your old password", status=status.HTTP_400_BAD_REQUEST)

  @action(detail=False, methods=['get', 'put'])
  def profile(self, request):
    user = request.user
    if user == AnonymousUser:
      return Response(data="Could not identfy user", status=status.HTTP_401_UNAUTHORIZED)
    profile = Profile.objects.get(user=user)
    if request.method == 'GET':
      serializer = ProfileSerializer(profile)
      return Response(serializer.data)
    elif request.method == 'PUT':
      data = request.data
      serializer = ProfileSerializer(profile, data)
      user_serializer = UserSerializer(user, data)
      user_serializer.is_valid(raise_exception=True)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      user_serializer.save()
      return Response(serializer.data)
  
  @action(detail=False, methods=['get','put'])
  def profilepic(self, request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'GET':
      img = profile.image
      print(type(img))
      if img:
        return FileResponse(img.open())
      else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
      data = request.data
      files = request.FILES
      profile.image = files.get('profilepic')
      profile.save()


    return Response("Yet to do")

  @action(detail=False, methods=['put'], permission_classes=[])
  def login(self, request):
    data = request.data
    user = authenticate(username=data.get('username'), password=data.get('password'))
    if user:
      token = Token.objects.filter(user=user)
      if token:
        # Remove old token and create a new one for this session
        token[0].delete()
      token = Token.objects.create(user=user)
      return Response(headers={'Access-Control-Expose-Headers': 'Authorization','Authorization' : token.key})
    else:
      return Response({"status" : "Invalid credentials" }, status=status.HTTP_400_BAD_REQUEST)
  
  @action(detail=False, methods=['put'], permission_classes=[])
  def register(self, request):
    data = {k:v for k,v in request.data.items() if not k == 'rePassword'} 
    try:
      user = User.objects.create_user(**data)
    except IntegrityError:
      return Response("That username is already taken", status=status.HTTP_400_BAD_REQUEST)
    except OperationalError:
      return Response("Something went wrong on our end, try again later", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
    return Response("User created!", status=status.HTTP_201_CREATED)
  

class BudgetViewSet(viewsets.ModelViewSet):
  queryset = Budget.objects.all()
  serializer_class = BudgetSerializer 


class StocksViewSet(viewsets.ModelViewSet):
  queryset = Stock.objects.all()
  serializer_class = StockSerializer
  