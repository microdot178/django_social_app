from rest_framework import serializers
from page.models import Post 


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'
		depth = 1