from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from utils.abstract import AbstractModel
from users.models import User


class Activity(AbstractModel):
    COMMENT = 'C'
    POST = 'P'
    USER_PAGE = 'U'
    ACTIVITY_TYPES = (
        (COMMENT, 'Comment'),
        (POST, 'Post'),
        (USER_PAGE, 'User page'),
    )
    user = models.ForeignKey(User, related_name="activities", on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    essence_id = models.PositiveIntegerField()
    essence_type = models.ForeignKey(ContentType, related_name="activities_content_type", on_delete=models.CASCADE)
    essence = GenericForeignKey('essence_type', 'essence_id')

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"


class Comment(AbstractModel):
    user = models.ForeignKey(User, related_name="comments_user", on_delete=models.CASCADE)
    text = models.TextField(max_length=600)
    comment = GenericRelation(Activity, related_query_name="comments")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Post(AbstractModel):
    user = models.ForeignKey(User, related_name="posts_user", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=600)
    image = models.ImageField(upload_to="post", blank=True)
    comment = GenericRelation(Activity, related_query_name="posts")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"Post (id: {self.id}):{self.title}"


class UserPage(AbstractModel):
    user = models.ForeignKey(User, related_name="userpages_user", on_delete=models.CASCADE)
    bio = models.CharField(max_length=70, blank=True)
    comment = GenericRelation(Activity, related_query_name="userpages")

    class Meta:
        verbose_name = "User Page"
        verbose_name_plural = "User Pages"

    def __str__(self):
        return f"Post (id: {self.id}):{self.user}"
