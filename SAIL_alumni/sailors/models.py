from django.db import models

class Sailor(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    graduation_year = models.IntegerField(null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    employment_status = models.CharField(
            max_length=255,
            choices=[
                ('employment', 'Employed'),
                ('unemployed', 'Unemployed'),
                ('student', 'Student'),
                ('freelance', 'Freelance'),
                ('self-employed', 'Self-employed'),
                ('other', 'Other')
            ],
            blank=True,
            null=True
    )
    job_title = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
