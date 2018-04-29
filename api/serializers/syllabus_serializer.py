from rest_framework import serializers

from ..models import Syllabus

class SyllabusSerializer(serializers.ModelSerializer):
    academic_credit_infos = serializers.SerializerMethodField()

    class Meta:
        model = Syllabus
        fields = (
            "title", "subject_code", "teacher_name", "academic_credit_infos",
            "target_class", "target_term", "class_number", "target_period",
            "published_date", "abstract", "positioning", "lecture_content",
            "lecture_processing", "performance_target", "valuation_basis",
            "instruction_out_learning", "keyword", "text_book", "study_aid_books",
            "notes", "professor_email",
        )
        # exclude = ('created_at',) # created_atのみ除く

    def get_academic_credit_infos(self, obj):
        infos = obj.academic_credit_infos.split("\n")

        rtn = []
        for info in infos:
            info = info.split(",")
            if len(info) == 3:
                rtn.append({
                    "target_participants": info[0],
                    "academic_credit_kind": info[1],
                    "academic_credit_num": float(info[2])
                })

        return rtn
