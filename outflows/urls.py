from django.urls import path
from . import views


urlpatterns = [
    path('outflows/list/', views.OutflowListView.as_view(),  name='outflow-list'),
    path('outflows/create/', views.OutflowCreateView.as_view(), name='outflow-create'),
    path('outflows/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflow-detail'),
]
