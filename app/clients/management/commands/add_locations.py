from django.core.management.base import BaseCommand

from ...models import Location


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs["file_name"]
        with open(f"{file_name}") as file:
            for row in file:
                name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                Location.objects.get_or_create(
                    name=name,
                )
        self.stdout.write(self.style.SUCCESS("list of objects added"))