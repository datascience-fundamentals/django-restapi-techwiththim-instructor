from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        # model to seralize
        model = BlogPost
        # set fields to include during the serialization
        fields = ["id", "title", "content", "published_date"]
        # include just in the response but you shouldn't send it on request
        read_only_fields = ["published_date"]
