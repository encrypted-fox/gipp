from django.db import models
from django.contrib.auth.models import User
from constructorapi.models import *


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    block_id = models.ForeignKey(AddedBlocks, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE)
    body = models.TextField()
    datetime = models.DateTimeField()


