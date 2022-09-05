from .models import Student
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer



class StudentsViewSet(ModelViewSet):
    queryset=Student.objects.all()
  
    def get_serializer_class(self):
        return StudentSerializer
   # serializer_clss=StudentSerializer(queryset, many=True)
# Create your views here.
