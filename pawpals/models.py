from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# For anything related to the review portion of my project:
# I followed along with a Django tutorial series on YouTube
# By Corey Schafer because I have never used Django
# Or created a full-stack web application before.
# I used this assignment as an opportunity to learn it
# Because I believe it will be useful in the future!
# I also used Bootstrap as a resource to make the site visually appealing.
# Although I was following along, I made a bunch of modifications to his code to create it
# The way I wanted it, but I want to give him credit because I have learned a lot from him.
# Here is the link to the first video in his series: https://www.youtube.com/watch?v=UmljXZIypDc

# Each model is a new table added to the database for this project
# I did not directly use a database tool because Django generated the
# Database for me

# Model for reviews
class Review(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
# This is the SQL code created by this
#CREATE TABLE "pawpals_review" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(50) NOT NULL, "content" text NOT NULL, "date" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
#CREATE INDEX "pawpals_review_author_id_82211bf1" ON "pawpals_review" ("author_id");
#COMMIT;

# Model for dogs
class Dog(models.Model):
    name =  models.CharField(max_length = 50)
    picture = models.ImageField(upload_to = 'dog_pics')
    description = models.TextField()

    def __str__(self):
        return self.name
# Model for cats
class Cat(models.Model):
    name =  models.CharField(max_length = 50)
    picture = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name

# Model for bunnies
class Bunnie(models.Model):
    name =  models.CharField(max_length = 50)
    picture = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name
