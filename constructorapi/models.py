from django.db import models
from django.contrib.auth.models import User


class Sites(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    owner = models.ForeignKey(User, related_name="sites", on_delete=models.CASCADE)


class Statuses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)


class SiteStatuses(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.ForeignKey(Sites, on_delete=models.CASCADE)
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE)


class HtmlHeads(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.ForeignKey(Sites, on_delete=models.CASCADE)
    bode = models.TextField()


class Headers(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.ForeignKey(Sites, on_delete=models.CASCADE)
    body = models.TextField()


class Footers(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.ForeignKey(Sites, on_delete=models.CASCADE)
    body = models.TextField()


class Mains(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.ForeignKey(Sites, on_delete=models.CASCADE)
    body = models.TextField()


class AddedBlocks(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.ForeignKey(Sites, on_delete=models.CASCADE)
    body = models.TextField()


class BlockTemplates(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.ForeignKey(Sites, on_delete=models.CASCADE)
    body = models.TextField()

