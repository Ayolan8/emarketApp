from django.urls import path
from . import views

urlpatterns = [
    path('new/<int:int>', views.new_conversation, name='new'),
]