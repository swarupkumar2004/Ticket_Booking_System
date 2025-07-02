from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from .models import UserProfile, Booking
from django.contrib.auth.hashers import make_password, check_password
from django.utils.dateparse import parse_date, parse_time
import json

# ----------------------------
# ✅ API Views (For Thunder Client)
# ----------------------------

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = UserProfile.objects.create(
            email=data['email'],
            password=make_password(data['password']),
            first_name=data['first_name'],
            last_name=data['last_name'],
            address=data['address'],
            phone_no=data['phone_no'],
        )
        return JsonResponse({'status': 'User registered successfully'})
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = UserProfile.objects.get(email=data['email'])
            if check_password(data['password'], user.password):
                return JsonResponse({'status': 'Login successful', 'user_id': user.id})
            else:
                return JsonResponse({'status': 'Invalid password'}, status=400)
        except UserProfile.DoesNotExist:
            return JsonResponse({'status': 'User not found'}, status=404)
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)


@csrf_exempt
def create_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = UserProfile.objects.get(id=data['user_id'])
        booking = Booking.objects.create(
            user=user,
            service_name=data['service_name'],
            booking_date=parse_date(data['booking_date']),
            booking_time=parse_time(data['booking_time']),
        )
        return JsonResponse({'status': 'Booking created', 'booking_id': booking.id})
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)


@require_GET
def list_bookings(request):
    bookings = Booking.objects.select_related('user').all()
    data = [
        {
            'user': b.user.first_name,
            'service': b.service_name,
            'date': b.booking_date,
            'time': b.booking_time,
            'confirmed': b.is_confirmed
        }
        for b in bookings
    ]
    return JsonResponse({'bookings': data})


# ----------------------------
# ✅ Frontend Template Views (HTML Forms)
# ----------------------------

def register_view(request):
    if request.method == 'POST':
        UserProfile.objects.create(
            email=request.POST['email'],
            password=make_password(request.POST['password']),
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            address=request.POST['address'],
            phone_no=request.POST['phone_no'],
        )
        return redirect('login')
    return render(request, 'booking/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = UserProfile.objects.get(email=email)
            if check_password(password, user.password):
                return redirect(f'/book/?user_id={user.id}')
        except UserProfile.DoesNotExist:
            pass
    return render(request, 'booking/login.html')


def book_view(request):
    if request.method == 'POST':
        booking = Booking.objects.create(
            user_id=request.POST['user_id'],
            service_name=request.POST['service_name'],
            booking_date=parse_date(request.POST['booking_date']),
            booking_time=parse_time(request.POST['booking_time']),
        )
        return redirect('booking-detail', booking_id=booking.id)
    user_id = request.GET.get('user_id')
    return render(request, 'booking/book.html', {'user_id': user_id})


def booking_detail_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking/booking_detail.html', {'booking': booking})


def home_view(request):
    return HttpResponse("""
        <h2>Welcome to the Ticket Booking System</h2>
        <a href='/register/'>Register</a> | <a href='/login/'>Login</a>
    """)
