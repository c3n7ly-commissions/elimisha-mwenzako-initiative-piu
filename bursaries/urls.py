from django.urls import path
from .views import CreateBursaryApplicationView

urlpatterns = [
    path("create/", CreateBursaryApplicationView.as_view(), name="create"),
]
