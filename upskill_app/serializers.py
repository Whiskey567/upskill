from rest_framework import serializers
from upskill_app import models


class User(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class Course(serializers.ModelSerializer):
    user = User(many=True, read_only=True)

    class Meta:
        model = models.Course
        fields = '__all__'


class Lesson(serializers.ModelSerializer):

    class Meta:
        model = models.Lesson
        fields = '__all__'

class Enrollment(serializers.ModelSerializer):
    class Meta:
        model = models.Enrollment
        fields = '__all__'

class Payment(serializers.ModelSerializer):
    user = User(read_only=True)
    user_id = serializers.IntegerField(required=True)
    nds = serializers.SerializerMethodField()
    class Meta:
        model = models.Payment
        fields = '__all__'

    def get_nds(self, obj):
        return round(obj.amount * 0.2, 2)

class Quiz(serializers.ModelSerializer):
    course = Course(read_only=True)
    course_id = serializers.IntegerField(required=False, allow_null=True)
    class Meta:
        model = models.Quiz
        fields = '__all__'

class Result(serializers.ModelSerializer):
    class Meta:
        model = models.Result
        fields = '__all__'
