from rest_framework_mongoengine import serializers

from mongo_test.models import Finance, User


class UserS(serializers.DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FinanceS(serializers.DocumentSerializer):
    class Meta:
        model = Finance
        fields = '__all__'
