# jobs/serializers.py
from rest_framework import serializers
from django.utils.text import slugify
from .models import Job, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at']
        read_only_fields = ['slug']

    def create(self, validated_data):
        name = validated_data.get('name')
        validated_data['slug'] = slugify(name)
        return super().create(validated_data)
    

    
class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'slug', 'company_name', 'description', 'requirements',
            'salary_min', 'salary_max', 'job_type', 'category', 'category_id',
            'latitude', 'longitude', 'city', 'country', 'is_remote', 'is_active',
            'posted_by', 'posted_at', 'updated_at',
        ]
        read_only_fields = ['posted_by', 'posted_at', 'updated_at']

    def create(self, validated_data):
        cat_id = validated_data.pop('category_id', None)
        if cat_id:
            validated_data['category_id'] = cat_id
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['posted_by'] = request.user
        return super().create(validated_data)
    

