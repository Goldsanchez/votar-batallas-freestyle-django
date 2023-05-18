from django.urls import path, include
from rest_framework import routers
from django.contrib.auth.models import User
from . import views

router = routers.DefaultRouter()
router.register(r'competitions', views.CompetitionViewSet)
router.register(r'seasons', views.SeasonViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'freestylers', views.FreestylerViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'battles', views.BattleViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'tokens', views.TokenViewSet)

urlpatterns = [
    path("signup/", views.signup),
    path("login/", views.Login.as_view()),
    path("logout/", views.Logout.as_view()),
    path("test_token/", views.test_token),
    path("", include(router.urls)),  
]