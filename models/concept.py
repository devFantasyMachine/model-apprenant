from django.db import models

class concept(models.Model):
    name = models.CharField(max_length=100)
    concept_id = models.AutoField(primary_Key=True)
    subconcepts = models.ManyToManyField('Subconcept', related_name='concepts', blank=True)
    description = models.TextField()
    def __str__(self):
        return f"Concept: {self.name}"