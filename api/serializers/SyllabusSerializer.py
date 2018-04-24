from rest_framework import serializers

from ..models import Syllabus

class SyllabusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Syllabus
        fields = (
            'title', 'teacher_name', 'target_participants', 'academic_credit',
            'academic_credit_num', 'target_class', 'target_term', 'class_number',
            'target_hour', 'target_place', 'published_date', 'abstract', 'positioning',
            'lecture_content', 'lecture_processing', 'performance_target',
            'valuation_basis', 'instruction_out_learning', 'keyword', 'text_book',
            'study_aid_books', 'notes', 'professor_email',
        )
