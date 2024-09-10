from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.


class About(models.Model):
    """
    Store a single page About the site
    """

    title = models.CharField(max_length=200)
    profile_image = CloudinaryField("image", default="placeholder")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        db_table = "about"

        verbose_name = "About section"
        verbose_name_plural = "About sections"

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Stores a single collaboration request message
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Collaboration Request"
        verbose_name_plural = "Collaboration Requests"

    def __str__(self):
        return f"Collaboration request from {self.name}"
