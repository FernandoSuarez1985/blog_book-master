from django.urls import path
from books.views import books, book_create, books_list, authors_list, author_create, editorials_list, editorial_create,genres_list, genre_create, books_search, contact


urlpatterns =[
    path('', books, name = 'books'),
    path('listar-libros/', books_list, name = 'books_list'),
    path('crear-libro/', book_create, name = 'book_create'),
    path('listar-autores/', authors_list, name = 'authors_list'),
    path('crear-autor/', author_create, name = 'author_create'),
    path('listar-editoriales', editorials_list, name = 'editorials_list'),
    path('crear-editorial/', editorial_create, name = 'editorial_create'),
    path('listar-generos/', genres_list, name = 'genres_list'),
    path('crear-genero/', genre_create, name = 'genre_create'),
    path('buscar-libros/', books_search, name = 'books_search'),
    path('contacto/', contact, name = 'contact')
]
