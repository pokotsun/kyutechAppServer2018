from django.core.management.base import BaseCommand, CommandError
from api.management.commands.lib.initialization import init_school_years
from api.models import SchoolYear

class Command(BaseCommand):
    help = "SchoolYearの初期化を行う" 

    def handle(self, *args, **options):
        init_school_years()