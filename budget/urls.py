from rest_framework.routers import DefaultRouter
from .views import BudgetView, ExpenseView, IncomeView, CategoryView

router = DefaultRouter(
    trailing_slash=False,
)
app_name = "budget"
router.register(
    'budget/?', BudgetView, basename='budget',
)
router.register(
    'income/?', IncomeView, basename='income',
)
router.register(
    'expense/?', ExpenseView, basename='expense',
)
router.register(
    'category/?', CategoryView, basename='category',
)

urlpatterns = router.urls
