from django.urls import path, include
from api.views import CommentAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'comment', CommentAPI, 'comment-api')

urlpatterns = [
    path('', include(router.urls))
]