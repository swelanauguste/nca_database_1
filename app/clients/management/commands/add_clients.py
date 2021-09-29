# from django.core.management.base import BaseCommand

# from ...models import Client


# class Command(BaseCommand):
#     def add_arguments(self, parser):
#         parser.add_argument("file_name", type=str)

#     def handle(self, *args, **kwargs):
#         file_name = kwargs["file_name"]
#         with open(f"{file_name}") as file:
#             for row in file:
#                 name = row.lower().replace("\n", "")
#                 self.stdout.write(self.style.SUCCESS(f"{name} added"))
#                 Client.objects.get_or_create(
#                     name=name,
#                 )
#         self.stdout.write(self.style.SUCCESS("list of objects added"))


import csv

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from ...models import Client


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
                    client_id = row[0]
                    name = row[1]
                    self.stdout.write(self.style.SUCCESS(f"{client_id}, {name} added"))
                    user = Client.objects.get_or_create(client_id=client_id, name=name)
