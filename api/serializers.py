from rest_framework import serializers

from .models import Card,Settings
class CardSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=100)
    answer = serializers.CharField(max_length=100)
    def create(self,validated_data):
        return Card.objects.create(**validated_data)
class CardGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id','question','answer','interval','last_learned']
class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    correct = serializers.CharField(max_length=100)
class SettingSerializer(serializers.Serializer):
    study_time = serializers.TimeField()
    questions_per_day = serializers.IntegerField()
class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()