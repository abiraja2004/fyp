from django.contrib import admin
from .models import Post
from .models import Quotation
# model registeration

admin.site.register([Post, Quotation])