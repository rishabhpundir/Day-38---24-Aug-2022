from django.urls import path, include
from apiapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('singers', views.SingerView, basename='singers')
router.register('songs', views.SongView, basename='songs')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterView.as_view()),
]