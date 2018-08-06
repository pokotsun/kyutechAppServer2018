from django.core.management.base import BaseCommand, CommandError
from api.management.commands.lib.initialization import initialize_syllabus
from api.models import Syllabus

class Command(BaseCommand):

    def handle(self, *args, **options):
        syllabuses = Syllabus.objects.all()
        rtn = {}
        print(f"{len(syllabuses)}件のシラバスから取得します")
        for syllabus in syllabuses:
            infos = syllabus.academic_credit_infos.split("\n")
            print(f"{syllabus.academic_credit_infos}")

            for info in infos:
                if info != "":
                    info_list = info.split(",")
                    data = info_list[0]
                    if data in rtn:
                        rtn[data] = rtn[data]+1
                    else:
                        rtn[data]=0

        with open("target_participants2.txt", "w") as f:
            for (k,v) in rtn.items():
                f.write(f"{k}: {v}\n")
                #f.write(f"{k}\n")
