from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return f"{self.name.capitalize()}"


class Staff(models.Model):
    class Position(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    position = models.CharField(max_length=30)
    salary = models.IntegerField()
    age = models.IntegerField()
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="staff"
    )

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()} {self.middle_name.capitalize()}"

    class Meta:
        indexes = [
            models.Index(fields=["last_name"]),
        ]
