from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signIn', views.signIn, name='signIn'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('statements', views.statements, name='statements'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('paypal-return/', views.PaypalReturnView.as_view(), name='paypal-return'),
    path('paypal-cancel/', views.PaypalCancelView.as_view(), name='paypal-cancel'),
    path('scores', views.Scores, name="scores"),
]