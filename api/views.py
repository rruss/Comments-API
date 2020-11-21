from django.core.paginator import Paginator
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from users.models import User

from .models import Comment, Post, Activity, UserPage
from .serializers import CommentSerializer


class CommentAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer

    @action(methods=['get'], detail=False)
    def paginate(self, data):
        essence = request.data["essence"]
        activity_type = request.data["activity_type"]

        if activity_type == "C":
            comment = Comment.objects.get(id=essence["id"])
            comments = comment.comment.all()

        elif activity_type == "P":
            post = Post.objects.get(id=essence["id"])
            comments = post.comment.all()

        elif activity_type == "U":
            userpage = UserPage.objects.get(id=essence["id"])
            comments = userpage.comment.all()

        else:
            return KeyError("Couldn't find data for provided activity type",
                            status.HTTP_400_BAD_REQUEST)

        paginator = Paginator(comments, 10)
        page = self.request.query_params.get('page')
        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)
        serializer = CommentSerializer(comments, many=True,)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def list(self, request, *args, **kwargs):
        essence = request.data["essence"]
        activity_type = request.data["activity_type"]

        if activity_type == "C":
            comment = Comment.objects.get(id=essence["id"])
            queryset = Comment.objects.filter(comment=comment)

        elif activity_type == "P":
            post = Post.objects.get(id=essence["id"])
            queryset = Comment.objects.filter(user__posts_user=post)

        elif activity_type == "U":
            userpage = UserPage.objects.get(id=essence["id"])
            queryset = Comment.objects.filter(user__userpages_user=userpage)

        else:
            return KeyError("Couldn't find data for provided activity type",
                            status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs['comment_id'])
        try:
            user = self.request.data["user"]
            serializer = CommentSerializer(comment)
            return Response(serializer.data)

        except KeyError:
            return Response("Couldn't find data for provided user", status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        try:
            username = request.data["user"]
            user = User.objects.get(username)
            essence = request.data["essence"]
            activity_type = request.data["activity_type"]
            comment = request.data["comment"]

            serializer = self.get_serializer(data=comment)
            serializer.is_valid(raise_exception=True)

            if activity_type == "C":
                comment = Comment.objects.get(id=essence["id"])
                comment.comment.create(activity_type=activity_type, user=user)

            elif activity_type == "P":
                post = Post.objects.get(id=essence["id"])
                post.comment.create(activity_type=activity_type, user=user)

            elif activity_type == "U":
                userpage = UserPage.objects.get(id=essence["id"])
                userpage.comment.create(activity_type=activity_type, user=user)

            self.perform_create(serializer)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except KeyError:
            return Response("Couldn't find data for provided user",
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        update_data = request.data["comment"]
        comment = get_object_or_404(Comment, pk=update_data["id"])
        serializer = CommentSerializer(comment, data=update_data)

        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionDetailPageSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=request.data["comment"]["id"])
        if comment.commet.count() == 0:
            comment.delete()
            return Response("Comment deleted", status=status.HTTP_204_NO_CONTENT)
        return Response("comment have child comments", status=status.HTTP_406_NOT_ACCEPTABLE)
