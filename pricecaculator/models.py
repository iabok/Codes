from django.core.urlresolvers import reverse
from django.db import models

__author__ = 'isaac'

# Create your models here.
USE_CATEGORIES = (
    ('National', 'National'),
    ('Regional', 'Regional'),
    ('National + Regional', 'National + Regional'),
    ('Published Magazine', 'Published Magazine'),
    ('Consumer Magazine', 'Consumer Magazine'),
    ('Text Publishing', 'Text Publishing'),
    ('Secondary Use', 'Secondary Use'),
    ('Homepage Use', 'Homepage Use'),

)

PLACEMENT_CATEGORIES = (
    ('Inside', 'Inside'),
    ('Cover', 'Cover'),
    ('Spot', 'Spot'),
)


SIZE_CATEGORIES = (
    ('1/16', '1/16'),
    ('1/8', '1/8'),
    ('1/4', '1/4'),
    ('1/2', '1/2'),
    ('Spot', 'Spot'),
    ('Small Size(250x250) Pixels', 'Small Size(250x250) Pixels'),
    ('Large Size(Over 250x250) Pixels', 'Large Size(Over 250x250) Pixels'),
    ('Full Page', 'Full Page'),
)


TERRITORY_CATEGORIES = (
    ('National', 'National'),
    ('Regional', 'Regional'),
    ('National + Regional', 'National + Regional'),
    ('Worldwide', 'Worldwide'),
)


PRINT_RUN_CATEGORIES = (
    ('5K', '5K'),
    ('10K', '10K'),
    ('25K', '25K'),
    ('100K', '100k'),
    ('250K', '250k'),
    ('Million', 'Million'),
    ('Up to a million', 'Up to a million'),
    ('Over to a million', 'Over to a million'),
)


DURATION_CATEGORIES = (
    ('1 Week', '1 Week'),
    ('1 Month', '1 Week'),
    ('3 Months', '3 Months'),
    ('1 Year', '1 Year'),
)


class Usage(models.Model):
    name = models.CharField(max_length=50, blank=False, help_text='*State the name of the Usage Plan Such as Newspaper,\
                                                                Magazines, Online usage etc.')
    slug = models.SlugField(max_length=50, blank=True, unique=True, help_text='*Unique value for the usage page URL\
                                                                created from name.')
    description = models.TextField(help_text='*Give a brief description of the of usage plan you are \
                                                                creating.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
            return reverse('usage', kwargs={'usage_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.name.lower().replace(" ", "-")
        super(Usage, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave usage."""
        super(Usage, self).delete(*args, **kwargs)


class Use(models.Model):
    usage = models.ForeignKey(Usage, null=True, blank=True)
    name = models.CharField(max_length=20, choices=USE_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Use, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave usage."""
        super(Use, self).delete(*args, **kwargs)


class Placement(models.Model):
    usage = models.ForeignKey(Usage, null=True, blank=True)
    name = models.CharField(max_length=20, choices=PLACEMENT_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Placement, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave usage."""
        super(Placement, self).delete(*args, **kwargs)


class Size(models.Model):
    usage = models.ForeignKey(Usage, null=True, blank=True)
    name = models.CharField(max_length=20, choices=SIZE_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Size, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave usage."""
        super(Size, self).delete(*args, **kwargs)


class Territory(models.Model):
    usage = models.ForeignKey(Usage, null=True, blank=True)
    name = models.CharField(max_length=20, choices=TERRITORY_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Territory, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave usage."""
        super(Territory, self).delete(*args, **kwargs)


class Duration(models.Model):
    usage = models.ForeignKey(Usage, null=True, blank=True)
    name = models.CharField(max_length=20, choices=DURATION_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Duration, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave usage."""
        super(Duration, self).delete(*args, **kwargs)


class PrintRun(models.Model):
    usage = models.ForeignKey(Usage, null=True, blank=True)
    name = models.CharField(max_length=20, choices=PRINT_RUN_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(PrintRun, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave usage."""
        super(PrintRun, self).delete(*args, **kwargs)
