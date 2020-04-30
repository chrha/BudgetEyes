from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db import IntegrityError, OperationalError
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token

from .models import Budget, Stock
from .serializers import BudgetSerializer, StockSerializer, UserSerializer
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
      return Response("The passwords you've entered does not match", status=status.HTTP_400_BAD_REQUEST)
    token = request.headers.get('Authorization').split(' ')[1]
    user = Token.objects.select_related('user').get(key=token).user
    print(pw, user)
    auth = user.check_password(pw)
    if not auth:
      user.set_password(pw)
      user.save()
      return Response(status=status.HTTP_202_ACCEPTED)
    else:
      return Response("You can't enter your old password", status=status.HTTP_400_BAD_REQUEST)

  @action(detail=False, methods=['put'], permission_classes=[])
  def login(self, request):
    data = request.data
    user = authenticate(username=data.get('username'), password=data.get('password'), request=request)
    if user:
      token = Token.objects.get(user=user)
      return Response(headers={'Authorization' : token.key})
    else:
      return Response("Invalid credentials", status=status.HTTP_400_BAD_REQUEST)
  
  @action(detail=False, methods=['put'], permission_classes=[])
  def register(self, request):
    data = request.data
    try:
      user = User.objects.create_user(**data)
      Token.objects.create(user=user)
    except IntegrityError:
      return Response("That username is already taken", status=status.HTTP_400_BAD_REQUEST)
    except OperationalError:
      # TODO: Remove user if it was created 
      return Response("Something went wrong on our end, try again later", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
    return Response("User created!", status=status.HTTP_201_CREATED)
  

class BudgetViewSet(viewsets.ModelViewSet):
  queryset = Budget.objects.all()
  serializer_class = BudgetSerializer 


class StocksViewSet(viewsets.ModelViewSet):
  queryset = Stock.objects.all()
  serializer_class = StockSerializer
  