from rest_framework.routers import DefaultRouter
from .views import BudgetView

router = DefaultRouter(
    trailing_slash=False,
)
# app_name = "api"
router.register(
    'budget/?', BudgetView, basename='budget'
)
urlpatterns = router.urls