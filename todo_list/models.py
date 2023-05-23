from django.db import models


class Task(models.Model):
    content = models.TextField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    experience_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tags")

    class Meta:
        ordering = ["done"]


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
