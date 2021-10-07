from django.contrib import admin
from django.urls import path
from question import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('practise_1/', views.practise_1),
    path('practise_2/', views.practise_2),
    path('Home/', views.Home.as_view()),
    path('HomeView/', views.HomeView.as_view())
]

