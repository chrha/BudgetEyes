from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'auth', views.UserViewSet)
router.register(r'stocks', views.StocksViewSet)
router.register(r'budget', views.BudgetViewSet)


urlpatterns = [
  path('',include(router.urls)),
]
