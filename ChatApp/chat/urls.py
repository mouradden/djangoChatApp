from django.urls import path, include
from chat import views as chat_views
# from django.contrib.auth.views import LoginView, LogoutView
# from .views import UserListView

from .views import login_view, index

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', index, name='index'),
    # path("", chat_views.chatPage, name="chat-page"),

    # # login-section
    # path("auth/login/", LoginView.as_view
    #      (template_name="chat/LoginPage.html"), name="login-user"),
    # path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    # path('api/users/', UserListView.as_view(), name='user-list'),
]
