from rest_framework import generics, viewsets

from ..models import Syllabus
from ..serializers import SyllabusSerializer

class SyllabusViewSet(viewsets.ModelViewSet):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer

class FilteredSyllabusViewSet(generics.ListAPIView):
    serializer_class = SyllabusSerializer

    def get_queryset(self):
        day = self.kwargs['day']
        period = str(self.kwargs['period'])
        # day = self.request.query_params.get('day', None)
        # period = self.request.query_params.get('period', None)

        if day is not None and period is not None:
            return Syllabus.filter_by_day_and_period(day, period)
        else:
            return None
