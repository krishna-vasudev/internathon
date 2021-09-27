from django.db import models
from datetime import datetime
from gdstorage.storage import GoogleDriveStorage
# Create your models here.
gd_storage = GoogleDriveStorage()

class Posts(models.Model):
    author=models.CharField(max_length=120)
    img = models.ImageField(upload_to='images/', storage=gd_storage,blank=True)
    date=models.DateTimeField(default=datetime.now,blank=True)
    description=models.TextField(blank=True)
    location=models.TextField(blank=True)
