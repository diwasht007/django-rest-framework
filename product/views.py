from django.shortcuts import render
from .models import Product, Store, Review
from product.api.serializers import ProductSerializer, StoreSerializer, ReviewSerializer
from .api.permission import AdminOrReadonlyPermission, ReviewUserorReadonlyPermission
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser,DjangoModelPermissions
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .api.throttling import ReviewDetailThrottle, ReviewListThrottle

 


# from rest_framework import mixins
from rest_framework import generics

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
       return Review.objects.all()
   
     
    def perform_create(self, serializer):
        pk= self.kwargs['pk']
        product = Product.objects.get(pk=pk)
        useredit = self.request.user
        Review_queryset = Review.objects.filter(product=product, apiuser=useredit)
        if Review_queryset.exists():
            raise ValidationError("You have already review this car")
        serializer.save(product=product,apiuser=useredit)


# class ReviewList(generics.ListCreateAPIView):
#     queryset= Review.objects.all()
#     serializer_class = ReviewSerializer

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    # authentication_classes = [JWTAuthentication]
    authentication_classes = [TokenAuthentication]

    # permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewListThrottle,AnonRateThrottle]
    def get_queryset(self):
        pk= self.kwargs['pk']
        return Review.objects.filter(product=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [AdminOrReadonlyPermission]
    permission_classes = [ReviewUserorReadonlyPermission]
    throttle_classes = [ReviewDetailThrottle,AnonRateThrottle]




    
    

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)



# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     # authentication_classes = [SessionAuthentication]
#     permission_classes = [DjangoModelPermissions]


    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class Store_Viewset(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

# class Store_Viewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Store.objects.all()
#         serializer = StoreSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Store.objects.all()
#         store_detail = get_object_or_404(queryset, pk=pk)
#         serializer = StoreSerializer(store_detail)
#         return Response(serializer.data)
    
#     def create(self,request,pk):
#         serializer = StoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





class store(APIView):
    def get(self,request):
        store = Store.objects.all()
        serializer = StoreSerializer(store, many=True,context={'request':request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StoreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class store_detail(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes =[IsAdminUser]
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAdminUser]


    def get(self,request,pk):
        try:
            store_detail = Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return Response({'error':'store not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = StoreSerializer(store_detail)
        return Response(serializer.data)
        
        
    def put(self,request,pk):
        store_detail = Store.objects.get(pk=pk)
        serializer = StoreSerializer(store_detail,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        store_detail = Store.objects.get(pk=pk)
        store_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['GET','POST'])
def product(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

@api_view(['GET','PUT','DELETE'])
def product_detail(request, pk):
    if request.method == 'GET':
        try:
            product_detail = Product.objects.get(pk=pk)
        except:
            return Response({'Error':'Product not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product_detail)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        product_detail = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product_detail,data = request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        product_detail = Product.objects.get(pk=pk)
        product_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


