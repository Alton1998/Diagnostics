from django.urls import path,include
from . import views
urlpatterns = [
    path('FertilityAPI/',views.FertilityAPIView.as_view())
]