import os
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        os.remove('media/files_2_upload/server_launch_.pdf')