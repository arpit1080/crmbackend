from django.db import models
from django.core.validators import MinLengthValidator, FileExtensionValidator 
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
import os


def validate_picture_size(value):
    max_size = 1024 * 1024     # Max size in bytes (1MB)
    if value.size > max_size:
        raise ValidationError(f"Max file size is {max_size} bytes")
    
def validate_picture_extension(value):
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    valid_extensions = ['.jpg', '.jpeg', '.png', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file format. Please upload a JPEG, PNG, or SVG file.')

class User(models.Model):
    Username = models.CharField(unique=True, max_length=150, blank=False)
    Profile_Photo = models.ImageField(upload_to='images/', validators=[validate_picture_size, FileExtensionValidator(['jpg', 'jpeg', 'png', 'svg'])], blank=True)
    First_Name = models.CharField(max_length=150, blank=False)
    Last_Name = models.CharField(max_length=150, blank=False) 
    Email = models.EmailField(unique=True, blank=False)
    Mobile_Number = models.CharField(max_length=10, validators=[MinLengthValidator(10)], unique=True)
    Role = models.CharField(max_length=150, blank=False)
    DOB = models.DateField(blank=False)
    Password = models.CharField(max_length=128, blank=False)
    Address = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # Check if the password has changed or it's a new record
        if self.pk is None or self._state.adding or self.Password != self.Confirm_Password:
            # Hash the password
            self.Password = make_password(self.Password)
        super().save(*args, **kwargs)
             
    class Meta:
        db_table = 'crm'

