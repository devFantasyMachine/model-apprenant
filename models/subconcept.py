from django.db import models
import concept
import evidence

class subconcept(models.Model):
    subconcept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    concept = models.ForeignKey(concept, on_delete=models.CASCADE, related_name='subconcepts')
    evidences = models.ManyToManyField(evidence, related_name='subconcepts', blank=True)

    def __str__(self):
        return f"Subconcept: {self.name} (belongs to {self.concept})"