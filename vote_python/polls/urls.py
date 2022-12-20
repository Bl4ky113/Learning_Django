from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_us, name='about_us'),
    path('<int:pk>/', views.detail_question, name='detail'),
    path('<int:pk>/results/', views.results_question, name='results'),
    path('<int:pk>/vote/', views.vote_question, name='vote')
]
