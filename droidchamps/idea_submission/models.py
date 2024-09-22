from django.db import models

# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    student_name = models.CharField(max_length=100)
    submission_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='idea_photos/', blank=True, null=True)

    def __str__(self):
        return self.title