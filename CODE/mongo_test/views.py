from rest_framework_mongoengine.viewsets import ModelViewSet

from mongo_test.models import User, Finance
from mongo_test.serializers import UserS, FinanceS
from mongo_test.filters import UserFilter, FinanceFilter


class UserVS(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserS
    # filter_class = UserFilter

    def filter_queryset(self, queryset):
        filter = UserFilter(self.request.query_params, queryset=queryset)
        return filter.qs


class FinanceVS(ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceS

    def filter_queryset(self, queryset):
        filter = FinanceFilter(self.request.query_params, queryset=queryset)
        return filter.qs
