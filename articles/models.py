from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    create_date = models.DateTimeField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:500]

    def published_date_pretty(self):
        return self.published_date.strftime('%b %e %Y')