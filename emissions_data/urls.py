from django.urls import path, include
from .views import EmissionView, CategoricalEmissions, ParametricEmissions, TemporalEmissions

urlpatterns = [
    path("countries/<int:country_id>/<int:start_year>/<int:end_year>/<str:categories>/", ParametricEmissions.as_view()),
    path("countries/<int:country_id>/<int:start_year>/<int:end_year>/", TemporalEmissions.as_view()),
    path("countries/<int:country_id>/<str:categories>/", CategoricalEmissions.as_view()),
    path("countries/", EmissionView.as_view()),
]

