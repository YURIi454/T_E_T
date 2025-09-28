from rest_framework import serializers


class TelegaIDSerializer(serializers.Serializer):
    """ Обработка поля ID. """

    telega_id = serializers.CharField(max_length=50)
