from core.models import Subscriber
from rest_framework.generics import CreateAPIView
from core.api.serializers import SubscriberSerializer


class SubscribeAPIView(CreateAPIView):
    serializer_class = SubscriberSerializer
    model = Subscriber



