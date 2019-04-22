import datetime

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models

class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be 2 or more characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to be 2 or more characters"
        if len(postData['first_name']) > 30:
            errors['first_name'] = "First name needs to be less then 30 characters"
        if len(postData['last_name']) > 30:
            errors['last_name'] = "Last name needs to be less then 30 characters"
        if not postData['first_name'].isalpha():
            errors['first_name'] = "First name needs to be only letters"
        if not postData['last_name'].isalpha():
            errors['last_name'] = "Last name needs to be only letters"

        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "Your email is not valid"
        else:
            if User.objects.filter(email=postData['email']):
                errors['email'] = "This email already exists"

        try:
            postData['username']
        except ValidationError:
            errors['username'] = "Your username is not valid"
        else:
            if User.objects.filter(username=postData['username']):
                errors['username'] = "This username already exists"

        if len(postData['password']) < 4:
            errors['password'] = "Please enter a longer password, needs to be four or more characters"
        if postData['password'] != postData['confirm_pass']:
            errors['confirm_pass'] = "Passwords must match"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    in_time = models.TimeField()
    is_in = models.BooleanField(default=False)
    out_time = models.TimeField()
    active = models.BooleanField(default=True)
    objects = UserManager()

class ClockEvent(models.Model):
    user = models.ForeignKey(User)

    def clockIn(self, user):
        self.user = user
        self.is_in = user.is_in
        self.in_time = user.in_time
        self.out_time = user.out_time
        self.user = user
        self.in_time = user.in_time =  datetime.datetime.now().strftime("%H:%M:%S")
        self.is_in = user.is_in = True

    def clockOut(self, user):
        self.user = user
        self.is_in = user.is_in
        self.in_time = user.in_time
        self.out_time = user.out_time
        self.out_time = user.out_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.is_in = user.is_in = False

class Points(models.Model):
    user = models.ForeignKey(User, verbose_name="user_points")
    points = models.IntegerField(default=0)

class DailyReport(models.Model):
    today = models.TextField()
    challenges = models.TextField()
    need_help = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

