from django.urls import path
from . import views

urlpatterns = [
    # API Endpoints
    path('', views.home_view, name='home'),
    path('api/register/', views.register_user),
    path('api/login/', views.login_user),
    path('api/book/', views.create_booking),
    path('api/bookings/', views.list_bookings),

    # Template-based views
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('book/', views.book_view, name='book'),
    path('booking-details/<int:booking_id>/', views.booking_detail_view, name='booking-detail'),

]
