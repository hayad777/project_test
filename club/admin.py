# club/admin.py
from django.contrib import admin
from .models import Program, Member  # Ensure Program is imported

admin.site.register(Program)  # Register Program model
admin.site.register(Member)  # Register Member model (if applicable)
