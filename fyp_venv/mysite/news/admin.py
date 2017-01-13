from django.contrib import admin
from .models import Post
from .models import Quotation
# Register your models here.

admin.site.register([Post, Quotation])