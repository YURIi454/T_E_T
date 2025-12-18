from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from tracker.models import Habit
from users.models import CustomUser


class HabitAPITestCase(APITestCase):
    """ Тест модели привычка. """

    def setUp(self):
        self.user = CustomUser.objects.create(email='test@test.com', password='test_pass123')
        self.client.login(email='test@test.com', password='test_pass123')
        self.client.force_authenticate(user=self.user)
        self.habit_data = {
            "place": "Где удобно",
            "time": "07:15:00",
            "action": "Кофе",
            "sign_pleasant": False,
            "period": 1,
            "award": "",
            "lead_time": 2,
            "is_public": True
        }

    def test_create_habit(self):
        url = reverse('tracker:habit_create')
        response = self.client.post(url, self.habit_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.get().action, 'Кофе')

    def test_get_habits_list(self):
        Habit.objects.create(user=self.user, **self.habit_data)
        url = reverse('tracker:habit_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_habit(self):
        habit = Habit.objects.create(user=self.user, **self.habit_data)
        url = reverse('tracker:habit_update', args=[habit.id])
        updated_data = {**self.habit_data, "action": "Прогулка"}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        habit.refresh_from_db()
        self.assertEqual(habit.action, 'Прогулка')

    def test_delete_habit(self):
        habit = Habit.objects.create(user=self.user, **self.habit_data)
        url = reverse('tracker:habit_delete', args=[habit.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)
