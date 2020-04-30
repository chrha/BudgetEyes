from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Budget, Stock 



class BudgetSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model = Budget
    fields = '__all__'


class StockSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Stock
    fields = ['name', 'value']

class UserSerializer(serializers.HyperlinkedModelSerializer):
  budget = serializers.SerializerMethodField()


  class Meta:
    model = User
    fields = ['id','first_name', 'last_name', 'username', 'email', 'budget']

  def get_budget(self, obj):
    budgets = Budget.objects.filter(owner=obj)
    if budgets:
      return budgets[0].jsonify()
    else:
      return ""
