from .views import CalculatorView, IndexView
from django.urls import path
app_name = "mathematic"


urlpatterns = [
    path("calculator/", CalculatorView.as_view(), name="calculator"),
    path("", IndexView.as_view(), name="index")
]