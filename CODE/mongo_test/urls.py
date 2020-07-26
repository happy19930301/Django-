from rest_framework.routers import DefaultRouter

from mongo_test.views import UserVS, FinanceVS

router = DefaultRouter()
router.register('user', UserVS, 'user')
router.register('finance', FinanceVS, 'finance')

urlpatterns = router.urls
