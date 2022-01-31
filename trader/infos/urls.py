from django.urls import path, include
from infos import views

urlpatterns = [
    path('V1/info/', views.Information.as_view()),
]
