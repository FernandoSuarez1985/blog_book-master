from django.contrib import admin
from books.models import Books, Authors, Editorials, Genres


admin.site.register(Books)
admin.site.register(Authors)
admin.site.register(Editorials)
admin.site.register(Genres)
