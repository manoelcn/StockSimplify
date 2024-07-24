from django.urls import path
from . import views


urlpatterns = [
    path('inflows/list/', views.InflowListView.as_view(),  name='inflow-list'),
    path('inflows/create/', views.InflowCreateView.as_view(), name='inflow-create'),
    path('inflows/<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflow-detail'),
]
