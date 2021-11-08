from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),

    path('', views.BookList.as_view(), name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name="book_detail"),
    path('add-book/', views.AddBook.as_view(), name='add_book'),
    path('edit-book/<int:pk>/', views.EditBook.as_view(), name="edit_book")
]