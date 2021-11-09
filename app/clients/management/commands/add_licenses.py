import csv

from django.core.management.base import BaseCommand

from ...models import License

# License.objects.all().delete()
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
                    license = row[0]
                    vending_fee = row[1]

                    self.stdout.write(self.style.SUCCESS(f"{license} added"))
                    License.objects.get_or_create(license=license, vending_fee=vending_fee)
