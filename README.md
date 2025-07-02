# Ticket_Booking_System
# 🎟️ Ticket Booking System

A full-stack Django-based ticket booking system that supports both API and web frontend interaction, built with Django, PostgreSQL, and Redis (Channels).

## 📌 Features

- ✅ User Registration (API + HTML Form)
- ✅ User Login (API + HTML Form)
- ✅ Ticket Booking with Date and Time (API + HTML Form)
- ✅ Booking Details View
- ✅ WebSocket Ready (Channels + Redis for future enhancements)

## 🛠️ Tech Stack

- **Backend:** Django 5.2.3
- **Database:** PostgreSQL
- **Real-time Layer:** Django Channels + Redis
- **Frontend:** HTML (Django Templates)
- **API Support:** JSON-based endpoints for register, login, and booking

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ticket-booking-system.git
cd ticket-booking-system
````

### 2. Create Virtual Environment

```bash
python -m venv myvenv
source myvenv/bin/activate    # On Windows: myvenv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL

Make sure PostgreSQL is running and a database named `ticketdb` is created.

Update credentials in `ticket_booking_system/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ticketdb',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Start Redis Server

Make sure Redis is running locally on port `6379`. If using Docker:

```bash
docker run -p 6379:6379 redis
```

### 7. Start Development Server

```bash
python manage.py runserver
```

---

## 🧪 API Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | `/api/register/` | Register user     |
| POST   | `/api/login/`    | Login user        |
| POST   | `/api/book/`     | Create a booking  |
| GET    | `/api/bookings/` | List all bookings |

### Example Request (Register)

```json
POST /api/register/
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "password": "123456",
  "address": "New York",
  "phone_no": "9876543210"
}
```

---

## 🌐 Web Pages

| URL                | Page                |
| ------------------ | ------------------- |
| `/`                | Home Page           |
| `/register/`       | Register Form       |
| `/login/`          | Login Form          |
| `/book/?user_id=1` | Booking Form        |
| `/booking/<id>/`   | Booking Detail Page |

---

## 📂 Project Structure

```
ticket_booking_system/
├── booking/
│   ├── templates/
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── book.html
│   │   └── booking_detail.html
│   ├── views.py
│   ├── models.py
│   ├── routing.py
│   └── urls.py
├── ticket_booking_system/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
├── manage.py
└── requirements.txt
```

---
