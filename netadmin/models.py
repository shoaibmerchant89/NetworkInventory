from django.db import models

# Create your models here.

class authors(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Authors"

class books(models.Model):

    name = models.CharField(max_length=50)
    isbn = models.IntegerField()
    author = models.ForeignKey(authors, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Books"

class fans(models.Model):

    name = models.CharField(max_length=50)
    author = models.ForeignKey(authors, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Fans"
