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

from .models import Budget, Stock, Profile, Expense
from .serializers import BudgetSerializer, StockSerializer, UserSerializer, ProfileSerializer, ExpenseSerializer
from .viewsets import CreateListUpdateViewSet
from .api import get_historical, parse_stock_data

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
    if request.data.get('password') != request.data.get('rePassword'):
      return Response("Passwords do not match", status=status.HTTP_400_BAD_REQUEST)
    data = {k:v for k,v in request.data.items() if not k == 'rePassword'}
    try:
      user = User.objects.create_user(**data)
      budget = Budget.objects.create(owner=user)
    except IntegrityError:
      return Response("That username is already taken", status=status.HTTP_400_BAD_REQUEST)
    except OperationalError:
      return Response("Something went wrong on our end, try again later", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response("User created!", status=status.HTTP_201_CREATED)


class BudgetViewSet(CreateListUpdateViewSet):
  queryset = Budget.objects.all()
  serializer_class = BudgetSerializer


  @action(detail=False, methods=['get', 'put'], permission_classes=[])
  def income(self, request):
    user = request.user
    if user == AnonymousUser:
        return Response(data="Could not identfy user", status=status.HTTP_401_UNAUTHORIZED)
    budget = Budget.objects.get(owner=user)
    if request.method == 'GET':
        serializer = BudgetSerializer(instance=budget, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
      data = request.data
      budget.income = data.get('income')
      budget.save()
    return Response("Yet to do")


  @action(detail=False, methods=['get', 'put'])
  def expenses(self, request):
    user = request.user
    if user == AnonymousUser:
        return Response(data="Could not identfy user", status=status.HTTP_401_UNAUTHORIZED)
    budget = Budget.objects.get(owner=user)
    expenses = Expense.objects.filter(budget=budget)
    if request.method == 'GET':
        serializer = ExpenseSerializer(instance=expenses, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        Expense.objects.filter(budget=budget).delete()
        data = request.data
        expenses = data.get('expenses')
        for e in expenses:
            expense = Expense.objects.create(budget=budget, sum=e.get('value'), name=e.get('name'))
    return Response("Yet to do")


class StocksViewSet(CreateListUpdateViewSet):
  queryset = Stock.objects.all()
  serializer_class = StockSerializer

  @action(detail=False, methods=['get'], permission_classes=[])
  def get_abbr(self, request):
    stocks=[{"name": s.name, "abbr":s.abbriev} for s in Stock.objects.all()]
    return Response(stocks, status=status.HTTP_200_OK)

  @action(detail=False, methods=['put'], permission_classes=[])
  def searches(self, request):
    data = request.data

    stock_name = request.data['stockname']
    search_data=str(stock_name)
    print(search_data)
    try:
      stock = Stock.objects.filter(name=search_data)
      if(not stock):
        print("Not here?")
        stock = Stock.objects.filter(abbriev=search_data)
        if(not stock):
          return Response(data="Could not identfy stock",status=status.HTTP_204_NO_CONTENT)
      tickers = [stock[0].abbriev]
      print(tickers)
      period = data.get('period', 7)

      if period == 1:
        is_daily = True
      else:
        is_daily = False
      print(tickers)
      data = get_historical(tickers=tickers, period=period)
      if len(tickers) == 1:
        parsed_data = parse_stock_data(data, name=tickers[0], is_daily=is_daily)
      else:
        parsed_data = parse_stock_data(data, is_daily=is_daily)
      if not parsed_data:
        return Response(status=status.HTTP_404_NOT_FOUND)
      return Response(parsed_data)
    except OperationalError:
      return Response("Something went wrong on our end, try again later", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  
  @action(detail=False ,methods=['put'], permission_classes=[])
  def query(self, request):
    data = request.data
    user = request.user
    if data.get('stocks') is None:
      if user == AnonymousUser:
        return Response("User not logged in, yet does not specify which stocks to see", status=status.HTTP_400_BAD_REQUEST)
      prof = Profile.objects.get(user=user)
      stocks = prof.stocks
      if not stocks.all():
        return Response("You are not following any stocks", status=status.HTTP_204_NO_CONTENT)
      tickers = [s.abbriev for s in stocks.all()]
    else:
      tickers = data.get('stocks')

    period = data.get('period', 7)
    if period == 1:
      is_daily = True
    else:
      is_daily = False
    data = get_historical(tickers=tickers, period=period)
    if len(tickers) == 1:
      parsed_data = parse_stock_data(data, name=tickers[0], is_daily=is_daily)
    else:
      parsed_data = parse_stock_data(data, is_daily=is_daily)
    
    if not parsed_data:
      return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(parsed_data)
