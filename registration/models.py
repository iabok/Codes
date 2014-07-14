from django.db import models

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


DIS_CHOICES = (
    ('No', 'No'),
    ('Yes', 'Yes'),
)

COUNTRY_CHOICES = (
    ('USA', 'USA'),
    ('UK', 'UK'),
    ('Uganda', 'Uganda'),
    ('Ghana', 'Ghana'),
    ('Germany', 'Germany'),
    ('France', 'France'),
    ('Italy', 'Italy'),
    ('Spain', 'Spain'),
    ('Portugal', 'Portugal'),
    ('Kenya', 'Kenya'),
    ('Tanzania', 'Tanzania'),
    ('South Africa', 'South Africa'),
)


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['-title']

    def __unicode__(self):
        return self.title, self.description


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.description


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe)
    number = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __unicode__(self):
        return self.number, self.description