from django.core.exceptions import ValidationError


def validate_habits(habit):
    """ Валидация привычек. """

    if habit.related_habit and habit.award:
        raise ValidationError(
            "В модели не должно быть заполнено одновременно и поле 'Вознаграждение', и поле 'Связанная привычка'. "
            "Можно заполнить только одно поле.")
    if habit.lead_time > 120:
        raise ValidationError("Время выполнения должно быть не больше 120 секунд.")
    if habit.sign_pleasant and (habit.award or habit.related_habit):
        raise ValidationError("У приятной привычки не может быть 'Вознаграждение' или 'Связанная привычка'.")
    if not (1 <= habit.period <= 7):
        raise ValidationError("Периодичность должна быть не меньше 1 и не больше 7 дней.")
