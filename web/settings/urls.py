from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Main.views import main
from Post.views import PostViewSet


app_name = 'settings'

router = DefaultRouter()
router.register(r'api/posts', PostViewSet, base_name='api_posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('social/', include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('api/v1', include(router.urls, namespace='api'))
]

urlpatterns += router.urls
