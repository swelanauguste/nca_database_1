import csv

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from ...models import Client, Gender, License, Location


def get_client_gender(pk):
    return Gender.objects.get(pk=pk)


def get_client_location(pk):
    return Location.objects.get(pk=pk)


def get_client_license(pk):
    return License.objects.get(pk=pk)


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
                    client = row[1]
                    gender = get_client_gender(row[3])
                    location = get_client_location(row[2])
                    # license = get_client_license(row[5])
                    # print("license", license, type(license))

                    tel = row[7]
                    national_insurance_id = row[8]
                    annual_venue_fee = row[9]

                    Client.objects.get_or_create(
                        client_id=client_id,
                        client=client,
                        location=location,
                        gender=gender,
                        tel=tel,
                        national_insurance_id=national_insurance_id,
                        # annual_venue_fee=annual_venue_fee,
                        # license=license,
                    )
                    self.stdout.write(self.style.SUCCESS(f"{client_id} added"))
