from django.urls import path
from . import views


app_name = 'main'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/', views.CreatePDFView.as_view(), name='pdf-create'),
    path('converter/', views.DashboardView.as_view(), name='pdf-home'),
    path('list/', views.PDFListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
]
