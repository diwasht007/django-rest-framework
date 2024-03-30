from rest_framework import serializers
from ..models import Product, Store, Review

# def alphanumeric(value):
#     if not str(value).isalnum():
#         raise serializers.ValidationError("only alphanumeric value are allowed")

class ReviewSerializer(serializers.ModelSerializer):
      class Meta:
            model = Review
            fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    Reviews = ReviewSerializer(many=True,read_only=True)
    # Reviews = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = "__all__"
        # exclude = ['image']

    def get_discounted_price(self,object):
            discountprice = object.price - 10
            return discountprice
    

    def validate_price(self, value):
            if value <= 100.00:
                raise serializers.ValidationError("price must be greater than 100.00")
            return value
        
    def validate(self, data):
            if data['product_name'] == data['description']:
                raise serializers.ValidationError(" name and description should be different")
            return data

class StoreSerializer(serializers.ModelSerializer):
      products = ProductSerializer(many=True, read_only=True)
    #   products = serializers.StringRelatedField(many=True)
    #   products = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    #   products = serializers.HyperlinkedRelatedField(many=True ,read_only=True, view_name='product_detail')

      class Meta:
            model = Store
            fields = "__all__"



      