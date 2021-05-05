from django.db import models


class SiteRelated(models.Model):
    """
    Adds a foreign key to Django's Site model.
    """

    site = models.ForeignKey("sites.Site", on_delete=models.CASCADE, editable=False)

    class Meta:
        abstract = True
