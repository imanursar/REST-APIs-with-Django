from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('SC','SCHOOL'),
    ('PS','PSYCHOLOGICAL'),
    ('CO','COMEDY'),
    ('SE','SEINEN'),
    ('RO','ROMANCE'),
)

LANGUAGE_CHOICES = (
    ('TV','TV'),
    ('MO','MOVIE'),
)

STATUS_CHOICES = (
    ('RA','RECENTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED'),
)

class Anime(models.Model):
    title = models.CharField(max_length=100)
    title_english = models.CharField(max_length=100,null=True)
    synonyms = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='movies')
    type_show = models.CharField(choices=LANGUAGE_CHOICES, max_length=2,null=True)
    episodes = models.IntegerField(default=12)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year_of_production = models.IntegerField()
    producers = models.CharField(max_length=50,null=True)
    duration = models.IntegerField(default=25)
    score = models.FloatField(default=0.0)
    ranked = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'animelist'
        #ordering = ['days_birth']

    def __str__(self):
        return f"{self.title} : {self.ranked} : {self.year_of_production}"
