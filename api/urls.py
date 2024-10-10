from django.urls import path, include
from . import views
urlpatterns = [
    path("api/contacts/", views.contactForm, name="valoris-contact-form")
]
