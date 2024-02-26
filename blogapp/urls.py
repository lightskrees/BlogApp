"""
URL configuration for blogapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import BlogViewSet, UserViewSet
from authentication.views import LoginPageView, SignupPageView, LogoutPageView, UploadProfileView
from blog.views import HomePageView, BlogUploadView, UserListView, BlogView, UserBlogView, GroupPostView

router = routers.SimpleRouter()

router.register('blog', BlogViewSet, basename='category')
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginPageView.as_view(), name='login'),
    path('home/', HomePageView.as_view(), name='home'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('blog/<int:id>/', BlogView.as_view(), name='blog_view'),
    path('add_blog/', BlogUploadView.as_view(), name='add_blog'),
    path('view_users/', UserListView.as_view(), name='users_list'),
    path('upload_profile/', UploadProfileView.as_view(), name='upload_profile'),
    path('user_posts/<int:pk>/', UserBlogView.as_view(), name='user_blog'),
    path('group_post/', GroupPostView.as_view(), name='group_post'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_URL)
