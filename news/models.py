from django.db import models
from django.contrib.auth.models import User
from django.db. models import Sum
from django.db.models.functions import Coalesce



class Author(models.Model):  
    user = models.OneToOneField(User, on_delete = models.CASCADE) 
    rating= models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def update_rating(self):
        author_posts_rating = Post.objects.filter(author_id=self.pk).aggregate(
            post_rating_sum=Coalesce(Sum('rating') * 3, 0))
        author_comment_rating = Comment.objects.filter(user_id=self.user).aggregate(
            comments_rating_sum=Coalesce(Sum('rating'), 0))
        author_post_comment_rating = Comment.objects.filter(post__author__user=self.user).aggregate(
            comments_rating_sum=Coalesce(Sum('rating'), 0))
        self.rating = author_posts_rating['post_rating_sum'] + author_comment_rating['comments_rating_sum'] + author_post_comment_rating['comments_rating_sum']
        self.save()
        

class Category(models.Model):
    name = models.CharField(max_length = 30, unique = True)


class Post(models.Model):
    article = 'AR'
    news = 'NE'

    POST = [
    (news, 'Новость'),
    (article, 'Статья')
]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating= models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=2, choices=POST)
    text = models.TextField()
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124]


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
