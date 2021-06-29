
from io import BytesIO      #handle images
from PIL import Image
from django.db import models

class CatalogueModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        db_table = 'courses_catalogue'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class SubjectModel(models.Model):
    catalogue = models.ForeignKey(CatalogueModel, related_name='subjects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        db_table = 'courses_subject'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return f'/{self.catalogue.slug}/{self.slug}/'

class ClassModel(models.Model):
    subject = models.ForeignKey(SubjectModel, related_name='classes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1500)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        db_table = 'courses_class'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return f'/{self.catalogue.slug}/{self.subject.slug}/{self.slug}/'



