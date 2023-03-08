from django.contrib.auth.models import User
from django.db import models

from .post_model import Post


class Comment(models.Model):
    user = models.ForeignKey(User,related_name='comment_model', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_model', on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return '"{body}..." on {post_title} by {username}'.format(body=self.body[:20],
                                                                  post_title=self.post.title,
                                                                  username=self.user.username)
