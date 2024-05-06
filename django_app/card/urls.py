from django.urls import path
from .views import add_card, show_card, send_to_ceremeo, send_card

urlpatterns = [
    path('card', add_card, name='add_card'),
    path('send-card', send_card, name='send_card'),
    path('show-card/<int:pk>', show_card, name='show_card'),
    path('card/<int:pk>/ceremeo/<int:step_number>', send_to_ceremeo, name='send_to_ceremeo')
]