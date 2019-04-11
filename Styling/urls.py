from django.urls import path

from .views import GarmentsAPIListView, GarmentsAPIID

urlpatterns = [
    path("", GarmentsAPIListView.as_view(), name="results_api_list"),
    path("<int:pk>", GarmentsAPIID.as_view(), name="results_api_detail"),
]