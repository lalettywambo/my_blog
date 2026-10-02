from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

def __string__(self):
    return self.title


# CREATE TABLE post(
#    id INTEGER PRIMARY KEY,
#    title VARCHAR(255)
#  content TEXT
#)