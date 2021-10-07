from django.urls import path
from user import views
from rest_framework import routers
from user.views import Apple

urlpatterns = [
    path('register.html', views.Register.as_view()),
    path('Login/', views.Login.as_view()),
    path('Question/', views.Question.as_view()),
    path('Choice/', views.Choice.as_view()),
    path('Activity/', views.Activity.as_view()),
    path('Pager/', views.Pager.as_view({'get': 'list'})),
]

router = routers.SimpleRouter()
router.register(r'v1/tree',Apple)

urlpatterns += router.urls