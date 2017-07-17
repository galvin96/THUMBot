from django.conf.urls import include, url
from .views import THUMBotView

urlpatterns = [
    url(r'^bot/?$', THUMBotView.as_view()),
]