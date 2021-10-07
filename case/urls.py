from django.urls import path
from case import views
from rest_framework import routers
from case.views import TestCase

urlpatterns = [

    # path('books/(?P<pk>\d+)', views.Pear.as_view({'get': 'backend_case'})),

]

router = routers.SimpleRouter()
router.register(r'v1',TestCase)

urlpatterns += router.urls