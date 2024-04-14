from core.models import Orders, OrderLine
from rest_framework import generics
from ..serializers.order_serializers import OrderSerializer, OrderLineSerializer
from core.views import BaseAPIView


# Orders
class OrderCreate(BaseAPIView, generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderListCreate(BaseAPIView, generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroy(BaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'order_id'

class OrderRetrieve(BaseAPIView, generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'order_id'

class OrderList(BaseAPIView, generics.ListAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        queryset = Orders.objects.all()

        # Filter by user
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)

        # Sort by order attribute
        sort_by = self.request.query_params.get('sort_by', None)
        if sort_by is not None:
            descending = sort_by.startswith('-')
            field = sort_by.lstrip('-')
            queryset = queryset.order_by(f'{"-" if descending else ""}{field}')

        return queryset

# Order Line
class OrderLineCreate(BaseAPIView, generics.CreateAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    
class OrderLineListCreate(BaseAPIView, generics.ListCreateAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer

class OrderLineRetrieveUpdateDestroy(BaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    lookup_field = 'order_line_id'

class OrderLineRetrieve(BaseAPIView, generics.RetrieveAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    lookup_field = 'order_line_id'

class OrderLineList(BaseAPIView, generics.ListAPIView):
    serializer_class = OrderLineSerializer

    def get_queryset(self):
        queryset = OrderLine.objects.all()

        # Filter by order
        order = self.request.query_params.get('order', None)
        if order is not None:
            queryset = queryset.filter(order=order)

        # Sort by order line attribute
        sort_by = self.request.query_params.get('sort_by', None)
        if sort_by is not None:
            descending = sort_by.startswith('-')
            field = sort_by.lstrip('-')
            queryset = queryset.order_by(f'{"-" if descending else ""}{field}')

        return queryset