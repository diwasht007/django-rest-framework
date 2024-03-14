from rest_framework import serializers
from ..models import Product

def alphanumeric(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("only alphanumeric value are allowed")


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField()
    slug = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=9,decimal_places=2)
    stock = serializers.IntegerField()
    is_available = serializers.BooleanField()
    image = serializers.ImageField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    def create(self, validate_data):
        return Product.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.slug = validated_data.get('slug',instance.slug)
        instance.description = validated_data.get('description',instance.description)
        instance.pricr = validated_data.get('price',instance.price)
        instance.stock = validated_data.get('stock',instance.stock)
        instance.image = validated_data.get('image',instance.image)
        instance.is_available = validated_data.get('is_available',instance.is_available)
        instance.save()
        return instance
    
    def validated_price(self, value):
        if value <= 100.00:
            raise serializers.ValidationError("price must be greater than 100.00")
        return value
    
    def validate(self, data):
        if data['product_name'] == data['description']:
            raise serializers.ValidationError(" name and description should be different")
        return data
    