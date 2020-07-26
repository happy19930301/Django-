import django_mongoengine_filter as filters

from mongo_test.models import User, Finance


class UserFilter(filters.FilterSet):
    descirption__a = filters.MethodFilter(action='descirption__a_filter')

    class Meta:
        model = User
        fields = ['name', 'descirption']

    def descirption__a_filter(self, queryset, descirption__a, value):
        return queryset.filter(descirption__a=int(value))


class FinanceFilter(filters.FilterSet):

    class Meta:
        model = Finance
        fields = ['is_invested', 'number']
