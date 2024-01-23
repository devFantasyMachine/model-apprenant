from django.db import models
import subconcept

class evidence(models.Model):
    evidence_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    Subconcept = models.ForeignKey(subconcept, on_delete=models.CASCADE, related_name='evidences')
    description = models.TextField()

    def __str__(self):
        return f"Evidence: {self.name} (Belongs to {self.Subconcept})"
    