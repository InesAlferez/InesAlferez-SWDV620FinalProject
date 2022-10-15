from django.urls import path
from . import views

urlpatterns = [
    path('leaveRequest/', views.leave_request),
]
