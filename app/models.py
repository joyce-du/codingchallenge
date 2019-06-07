from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    description = models.TextField()
    author = models.CharField(max_length=200)
    tags = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_edit', kwargs={'pk': self.pk})
