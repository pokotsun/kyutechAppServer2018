from rest_framework import generics, viewsets

from ..models import Syllabus
from ..serializers.SyllabusSerializer import SyllabusSerializer

class SyllabusViewSet(viewsets.ModelViewSet):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer

class FilteredSyllabusViewSet(generics.ListAPIView):
    def get_queryset(self):
        if date_param is not None:
            return 0
