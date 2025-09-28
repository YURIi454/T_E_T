from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView)
from rest_framework.permissions import IsAuthenticated, AllowAny

from tracker.models import Habit
from tracker.serializers import HabitSerializer
from users.permissions import OwnerOrReadOnlyPerm, OwnerOnlyPerm


class HabitCreateAPIView(CreateAPIView):
    """ Создание привычки. """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

    def perform_create(self, serializer):
        """ Сохраняет привычку текущего пользователя. """

        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(ListAPIView):
    """ Список привычек. """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user).order_by("id")


class HabitRetrieveAPIView(RetrieveAPIView):
    """ Доступ только владельцам. """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, OwnerOrReadOnlyPerm]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPUView(UpdateAPIView):
    """ Обновление привычки только владельцем. """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, OwnerOnlyPerm]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDestroyAPIView(DestroyAPIView):
    """ Удаление привычки только владельцем. """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, OwnerOnlyPerm]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListAPIView(ListAPIView):
    """ Позволяет всем пользователям видеть список публичных привычек. """

    serializer_class = HabitSerializer
    permission_classes = [AllowAny]
    queryset = Habit.objects.filter(is_public=True).order_by("id")
    filter_backends = [DjangoFilterBackend]
