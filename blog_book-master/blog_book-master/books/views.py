from cgi import print_exception
from django.shortcuts import render
from django.http import HttpResponse
from books.models import Books, Authors, Editorials, Genres
from books.forms import Books_form, Authors_form, Editorials_form, Genres_Form


def books(request):
    return render(request, 'books.html')


def books_list(request):
    books = Books.objects.all()
    context = {'books': books}
    return render(request, 'books-list.html', context = context)


def book_create(request):
    if request.method == 'GET':
        form = Books_form()
        context = {'form' : form}
        return render(request, 'book-create.html', context = context)
    else:
        form = Books_form(request.POST)
        if form.is_valid():
            new_book = Books.objects.create(
                isbn = form.cleaned_data['isbn'],
                title = form.cleaned_data['title'],
                synopsis = form.cleaned_data['synopsis'],
                publication_date = form.cleaned_data['publication_date'],
                edition = form.cleaned_data['edition'],
                price = form.cleaned_data['price'],
                active = form.cleaned_data['active']
            )
            context = {'new_book' : new_book}
        return render(request, 'book-create.html', context = context)


def authors_list(request):
    authors = Authors.objects.all()
    context = {'authors': authors}
    return render(request, 'authors-list.html', context = context)


def author_create(request):
    if request.method == 'GET':
        form = Authors_form()
        context = {'form' : form}
        return render(request, 'author-create.html', context=context)
    else:
        form = Authors_form(request.POST)
        if form.is_valid():
            new_author = Authors.objects.create(
                id = form.cleaned_data['id'],
                name = form.cleaned_data['name'],
                middle_name = form.cleaned_data['middle_name'],
                surname = form.cleaned_data['surname'],
                nickname = form.cleaned_data['nickname'],
                birthday = form.cleaned_data['birthday'],
                active = form.cleaned_data['active']
            )
            context = {'new_author': new_author}
        return render(request, 'author-create.html', context = context)


def editorials_list(request):
    editorials = Editorials.objects.all()
    context = {'editorials': editorials}
    return render(request, 'editorials-list.html', context = context)

def editorial_create(request):
    if request.method == 'GET':
        form = Editorials_form()
        context = {'form' : form}
        return render(request, 'editorial-create.html', context = context)
    else:
        form = Editorials_form(request.POST)
        if form.is_valid():
            new_editorial = Editorials.objects.create(
                id = form.cleaned_data['id'],
                name = form.cleaned_data['name'],
                founder = form.cleaned_data['founder'],
                foundation_date = form.cleaned_data['foundation_date'],
                country = form.cleaned_data['country'],
                main_organization = form.cleaned_data['main_organization'],
                active = form.cleaned_data['active']
            )
            context = {'new_editorial' : new_editorial}
        return render(request, 'editorial-create.html', context = context)


def genres_list(request):
    genres = Genres.objects.all()
    context = {'genres': genres}
    return render(request, 'genres-list.html', context = context)


def genre_create(request):
    if request.method == 'GET':
        form = Genres_Form()
        context = {'form' : form}
        return render(request, 'genre-create.html', context=context)
    else:
        form = Genres_Form(request.POST)
        if form.is_valid():
            new_genre = Genres.objects.create(
                id = form.cleaned_data['id'],
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                active = form.cleaned_data['active']
            )
            context = {'new_genre': new_genre}
        return render(request, 'genre-create.html', context = context)


def contact(request):
    return render(request, 'contact.html')


def books_search(request):
    print(request.GET)
    # books = Books.objects.get()
    books = Books.objects.filter(title__contains = request.GET['search'])
    context = {'books' : books}
    return render(request, 'books-search.html', context = context)
