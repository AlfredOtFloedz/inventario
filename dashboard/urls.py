from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('producto/', views.producto, name='dashboard-producto'),
    path('producto/delete/<int:pk>/', views.producto_delete, name='dashboard-producto-delete'),
    path('producto/update/<int:pk>/', views.producto_update, name='dashboard-producto-update'),
    path('pedido/', views.order, name='dashboard-order'),
    path('precio/', views.precio, name='dashboard-precio'),
    path('producto_csv/', views.producto_csv, name='dashboard-producto-csv'),
    path('pedido_csv/', views.order_csv, name='dashboard-order-csv') 
]
