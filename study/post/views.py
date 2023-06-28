from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Category, Comment
from user.models import User
from .serializers import PostSerializer, CommentSerializer

# Post CRUD 구현    
class PostCreate(APIView):
    # request = [title, content]
    def post(self, request):
        post = Post()

        post.title = request.data["title"]
        post.content = request.data["content"]
        post.writer = request.user
        post.save()

        postSerializer = PostSerializer(post)
        return Response(postSerializer.data, status=200)   

class PostRead(APIView):
    def get(self, request):
        posts = Post.objects.all()
        
        postSerializer = PostSerializer(posts, many=True)
        return Response(postSerializer.data, status=200)   

class PostUpdate(APIView):
    # request = [id, title, content]
    def put(self, request):
        # post = Post.objects.filter(id = request.data[id])
        post = get_object_or_404(Post, pk = id)

        post.title = request.data["title"]
        post.content = request.data["content"]
        post.save()

        postSerializer = PostSerializer(post)
        return Response(postSerializer.data, status=200)    

class PostDelete(APIView):
    # request = [id]
    def delete(self, request):
        post = Post.objects.filter(id = request.data[id])

        post.delete()
        
        return Response(status=200)
    

# Comment CRUD 구현
class CommentCreate(APIView):
    # request = [content]
    def post(self, request):
        comment = Comment()

        comment.content = request.data["content"]
        comment.writer = request.user
        comment.save()

        commentSerializer = CommentSerializer(comment)
        return Response(commentSerializer.data, status=200)
    
class CommentRead(APIView):
    def get(self, request):
        comments = Comment.objects.all()

        commentSerializer = CommentSerializer(comments, many=True)
        return Response(commentSerializer.data, status=200)

class CommentUpdate(APIView):
    # request = [content]
    def put(self, request):
        comment = Comment.objects.filter(id = request.data[id])

        comment.content = request.data["content"]
        comment.save()

class CommentDelete(APIView):
    # request = [id]
    def delete(self, request):
        comment = Comment.objects.filter(id = request.data[id])

        comment.delete()
        
        return Response(status=200)



# 1. '카테고리별' 게시글 작성
class Q1(APIView):
    # request = [title, content, category]
    def post(self, request):
        post = Post()

        post.title = request.data["title"]
        post.content = request.data["content"]
        post.writer = request.user
        
        # 존재하는 Category
        if (Category.objects.filter(name = request.data["category"])):
            post.category = Category.objects.get(name = request.data["category"])
        
        # 존재하지 않는 Category
        else:
            category = Category()
            category.name = request.data["category"]
            category.save()

            post.category = category

        post.save()

        postSerializer = PostSerializer(post)
        return Response(postSerializer.data, status=200)   

# 2. '카테고리별' 게시글 조회
class Q2(APIView):
    # request = [category]
    def get(self, request):
        categoryObj = Category.objects.get(name = request.data["category"])

        posts = Post.objects.filter(category = categoryObj)
        
        postSerializer = PostSerializer(posts, many=True)
        return Response(postSerializer.data, status=200) 

# 3. '내'가 작성한 게시글 조회
class Q3(APIView):
    def get(self, request):
        posts = Post.objects.filter(writer = request.user)

        postSerializer = PostSerializer(posts, many=True)
        return Response(postSerializer.data, status=200) 

# 4. '내'가 작성한 댓글 조회
class Q4(APIView):
    def get(self, request):
        comments = Comment.objects.filter(writer = request.user)

        commentSerializer = CommentSerializer(comments, many=True)
        return Response(commentSerializer.data, status=200)
    
# 5. '특정 유저'가 작성한 댓글 조회
class Q5(APIView):
    # request = [(user)id]
    def get(self, request):
        user = User.objects.get(id = request.data["id"])
        comments = Comment.objects.filter(writer = user)
        commentSerializer = CommentSerializer(comments, many=True)
        return Response(commentSerializer.data, status=200)

# 6. 게시글 좋아요 기능
class Q6(APIView):
    # request = [(post)id]
    def post(self, request):
        post = Post.objects.get(id = request.data["id"])

        # 취소
        if request.user in post.like.all():
            post.like.remove(request.user)
        
        # 추가
        else:
            post.like.add(request.user)

        # 개수
        return Response({"message": post.like.count()})





