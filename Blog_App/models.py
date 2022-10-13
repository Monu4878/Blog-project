
from django.db import models

# Create your models here.
class Blogging(models.Model):
    blog_heading=models.CharField(max_length=100)
    blog_images=models.ImageField(upload_to='Blog_images')
    blog_desc=models.CharField(max_length=1000)
    pub_date=models.DateTimeField(auto_now_add=True)
    pub_name=models.CharField(max_length=100)

    def __str__(self):
        return self .blog_heading
    