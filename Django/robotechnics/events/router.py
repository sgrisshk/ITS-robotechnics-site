from django.shortcuts import get_object_or_404
from events.models import ClassicEvent
from events.pagination import ClassicEventPagination
from events.serializers import (ClassicEventByIdSerializer,
                                ClassicEventsSerializer)
from rest_framework import routers, viewsets
from rest_framework.response import Response


class ClassicEventViewSet(viewsets.ModelViewSet):
    """!
    @brief Роутер для классических мероприятий
    @details Нужен для автоматической маршрутизации
    @param queryset Список всех объектов из базы данных
    @param serializer_class Сериализатор
    """
    queryset = ClassicEvent.objects.all()
    serializer_class = ClassicEventsSerializer
    pagination_class = ClassicEventPagination

    def retrieve(self, request, pk=None):
        classic_event = get_object_or_404(self.queryset, pk=pk)
        serializer = ClassicEventByIdSerializer(classic_event)
        return Response(serializer.data)


router = routers.DefaultRouter()
router.register(r'', ClassicEventViewSet)
