from django.db import models

class Publisher(models.Model):
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

class Book(models.Model):
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
