from django.urls import path
from . import views

urlpatterns = [
    path('book/show/',views.book_list, name="books"),
    path('book/show/<str:pk>',views.book_details, name="book-details"),
    path('book/add/',views.add_book, name="add-book"),
    path('book/update/',views.update_book, name="add-book"),
    path('book/delete/',views.delete_book, name="delete-book"),
]