from django.db import models
from uuid import uuid4


# model Book
class Book(models.Model):

    release_year =(
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
    )

    book_id = models.UUIDField(primary_key=True, default=uuid4, editable=False) # primary key
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField()
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    pages = models.IntegerField()
    published = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    release_year = models.CharField(max_length=4, choices=release_year, default='2021')

    def __str__(self):
        return self.title[:30]
  