from django.urls import path

from .comment import CommentCreate
from .home import home
from .post import PostView, PostCreate, PostUpdate, PostDelete
from .views import *
app_name = 'social_network_core_app'
urlpatterns = [
    path('profile/',profile,name='profile'),
    path('', home, name='home'),
    path('<str:username>', home, name='user_posts'),
    path('post/<int:pk>/', PostView.as_view(), name='post'),
    path('post/create/', PostCreate.as_view(), name='create_post'),
    path('post/create/<int:pk>/update', PostUpdate.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='delete_post'),
    path('post/<int:pk>/comment/', CommentCreate.as_view(), name='create_comment'),
    # path('friend_request/<int:to_user_id>/', send_friend_request, name='send_friend_request'),
    # path('friend_request/accept/<int:friend_request_id>/', accept_friend_request, name='accept_friend_request'),

    path('room/<int:room_id>/', chat_room, name='chat_room'),
    path('message/create/', message_create, name='message_create'),
]
