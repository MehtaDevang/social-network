from django.db import models

# Create your models here.

class OurUsers(models.Model):
    name = models.CharField(max_length=30, null=False)
    dob = models.DateField(null=False)
    username = models.EmailField(max_length=50, primary_key=True, null=False)
    password = models.CharField(max_length=20, null=False)
    friends = models.ManyToManyField('self', null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return str(self.username)