from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes),

    # Separate functions with distinct endpoints:
    path("books/", views.getBooks, name="get-books"),                         # GET list
    path("books/create/", views.createBook, name="create-book"),              # POST create

    path("books/<str:pk>/", views.getBook, name="get-book"),                  # GET detail
    path("books/<str:pk>/update/", views.updateBook, name="update-book"),     # PUT update
    path("books/<str:pk>/delete/", views.deleteBook, name="delete-book"),     # DELETE
]
