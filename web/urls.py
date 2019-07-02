from django.urls import path

from . import views

app_name = 'web'
urlpatterns = [
    path('<int:question_id>/vote/',views.vote, name='vote')
]