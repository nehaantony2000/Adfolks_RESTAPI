from rest_framework import serializers
from .models import tbl_topics, tbl_comments

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_comments
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    comment=CommentSerializer(many=True, read_only=True)
    class Meta:
        model = tbl_topics
        fields = '__all__'