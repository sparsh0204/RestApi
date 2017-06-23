from rest_framework import viewsets
from .models import Datatable
from .serializers import DatatableSerializer, UserSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

# Create your views here.

class Datatablelist(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Datatable.objects.all()
    model = Datatable
    serializer_class = DatatableSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,)#(filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields =  ('text','data')
    search_fields = ('text',)
    ordering  = ('-number',)

    def get_queryset(self):
        queryset = self.model.objects.all().filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
