from django.urls import path
from qv1.views import Quizes
urlpatterns = [
    path('quizes/', Quizes.as_view(), name='quizes')
]