from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Author
from .models import Category
from .models import Rate
from .models import User



# Register your models here.



admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Rate)
admin.site.register(User)
