from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    # this links a userPRofile to a django User instance
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="profile_images", blank=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name



class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    wAnswer1 = models.CharField(max_length=255)
    wAnswer2 = models.CharField(max_length=255)
    wAnswer3 = models.CharField(max_length=255)
    correctAnswer = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class userScore(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.score
