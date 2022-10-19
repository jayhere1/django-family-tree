from django.urls import path
from .views import (
    PersonListApiView,
    PersonDetailApiView,
    PersonChildrenApiView,
    PersonSiblingsAPIView,
    PersonAncestorsAPIView,
    PersonDescendantsAPIView,
)

urlpatterns = [
    path("api/people", PersonListApiView.as_view()),
    path("api/people/<int:person_id>/", PersonDetailApiView.as_view()),
    path("api/people/<int:person_id>/children", PersonChildrenApiView.as_view()),
    path("api/people/<int:person_id>/siblings", PersonSiblingsAPIView.as_view()),
    path("api/people/<int:person_id>/ancestors", PersonAncestorsAPIView.as_view()),
    path("api/people/<int:person_id>/descendants", PersonDescendantsAPIView.as_view()),
]
