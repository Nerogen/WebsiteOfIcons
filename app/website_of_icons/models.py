from django.db import models

# Create your models here.


class Icons(models.Model):
    subject_matter = models.CharField("subject matter", max_length=100)
    icon = models.ImageField(upload_to='images/', null=True, max_length=255)

    def __repr__(self):
        return 'Image(%s, %s)' % (self.subject_matter, self.icon)

    def __str__(self):
        return self.subject_matter

    class Meta:
        verbose_name = "Icons"
