from django.db import models


class Role(models.Model):
    name = models.TextField(unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'role'


class Profile(models.Model):
    username = models.TextField(unique=True)
    description = models.TextField(null=True)
    password = models.TextField()
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    middle_name = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'profile'


class ProfileRole(models.Model):
    profile = models.ForeignKey(Profile)
    role = models.ForeignKey(Role)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'profile_role'
        unique_together = ('profile', 'role')
