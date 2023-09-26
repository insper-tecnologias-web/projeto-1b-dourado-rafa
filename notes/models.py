from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=15, default='Sem Tag')
    color = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} {self.name}'


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.id}. {self.title}'