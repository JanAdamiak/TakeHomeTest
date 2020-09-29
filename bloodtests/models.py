from django.db import models

class Test(models.Model):
    code = models.CharField(unique=True, max_length=4, null=False)
    name = models.CharField(max_length=100, null=False)
    unit = models.CharField(max_length=10, null=False)
    lower = models.FloatField(null=True)
    upper = models.FloatField(null=True)

    def __str__(self):
        return self.name

    def combined(self):
        if self.upper == None:
            return 'value >= 45.0'
        elif self.lower == None:
            return 'value <= 45.0'
        return f"{self.lower} <= value <= {self.upper}"

#class TestResult(models.Model):
#    sampletext = models.CharField(max_length=4)