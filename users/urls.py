from rest_framework.routers import DefaultRouter
from .views import UsersView

router = DefaultRouter(
    trailing_slash=False,
)

router.register(
    'user/?', UsersView, basename='users'
)
urlpatterns = router.urls