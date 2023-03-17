from django.urls import path
from server.apps.posts.views import posts_list, posts_retrieve, posts_create, posts_delete, posts_update
# from . import views 위랑 같은것 하지만 이렇게 사용하기 위해서는 밑에가 views.posts_list 가 되어야함. 

app_name='posts' #별칭이 posts 영역에서만 사용된다는걸 알려줌
 
urlpatterns= [
    path("", posts_list, name='list'),
    path("posts/create", posts_create , name='create'),
    path("posts/<int:pk>", posts_retrieve, name='retrieve'),
    path("posts/<int:pk>/update", posts_update , name='update'),
    path("posts/<int:pk>/delete", posts_delete,name='delete'),
]