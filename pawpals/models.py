from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

# This is the SQL code created by this
#CREATE TABLE "pawpals_review" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(50) NOT NULL, "content" text NOT NULL, "date" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
#CREATE INDEX "pawpals_review_author_id_82211bf1" ON "pawpals_review" ("author_id");
#COMMIT;

    def __str__(self):
        return self.title

class Dog(models.Model):
    name =  models.CharField(max_length = 50)
    picture = models.ImageField(upload_to = 'dog_pics')
    description = models.TextField()

    def __str__(self):
        return self.name

class Cat(models.Model):
    name =  models.CharField(max_length = 50)
    picture = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Bunnie(models.Model):
    name =  models.CharField(max_length = 50)
    picture = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name
