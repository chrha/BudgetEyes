from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Budget, Stock ,Expense, Profile



class BudgetSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Budget
    fields = '__all__'


class StockSerializer(serializers.ModelSerializer):

  class Meta:
    model = Stock
    fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):

  class Meta:
    model = Expense
    fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):

  def update(self, instance, validated_data):
    instance.first_name = validated_data.get('first_name', instance.first_name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.email = validated_data.get('email', instance.email)
    instance.save()

    return instance

  class Meta:
    model = User
    fields = ['id','first_name', 'last_name', 'username', 'email']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
  userinfo = serializers.SerializerMethodField()
  stocks = serializers.SerializerMethodField()

  def update(self, instance, validated_data):
    instance.birth_date = validated_data.get('birth_date', instance.birth_date)
    instance.bio = validated_data.get('bio', instance.bio)
    instance.city = validated_data.get('city', instance.city)
    instance.save()
    return instance

  class Meta:
    model = Profile
    fields = ['birth_date', 'bio', 'city', 'userinfo', 'stocks']

  def get_userinfo(self, obj):
    user = obj.user
    return {
      "first_name" : user.first_name,
      "last_name" : user.last_name,
      "date_joined": user.date_joined.date(),
      "email" : user.email,
    }
  def get_stocks(self, obj):
    return [StockSerializer(s).data for s in obj.stocks.all()]
