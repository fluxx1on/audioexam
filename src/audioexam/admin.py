from django.contrib import admin
from django.shortcuts import render, HttpResponseRedirect
from .models import *

admin.site.register(Document)
admin.site.register(Audio)