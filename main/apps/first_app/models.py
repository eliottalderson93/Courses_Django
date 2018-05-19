from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class coursesManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors["name"] = "course name should be at least 6 characters long"
        if len(postData['desc']) < 15:
            errors['desc'] = "description should be at least 15 characters long"
        # if not EMAIL_REGEX.match(postData['email']):
        #     errors['email'] = "invalid email"
        return errors
class courses(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = coursesManager()
    def __repr__(self):
        return "<course object: name: {} desc: {} created_at: {}".format(self.name, self.desc, self.created_at)
