from django.urls import path


from telega.views import TelegramChatIDUpdateAPIView

app_name = 'telega'

urlpatterns = [
    path('telega_chat_id/', TelegramChatIDUpdateAPIView.as_view(), name='telegram_chat_id_update'),
]
