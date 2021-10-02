import csv

from django.core.management.base import BaseCommand

from ...models import Location


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs["file_name"]
        with open(f"{file_name}", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    location = row[0]

                    self.stdout.write(self.style.SUCCESS(f"{location} added"))
                    Location.objects.get_or_create(location=location)
