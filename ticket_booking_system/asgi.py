# ticket_booking_system/asgi.py

"""
ASGI config for ticket_booking_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import booking.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticket_booking_system.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            booking.routing.websocket_urlpatterns
        )
    ),
})