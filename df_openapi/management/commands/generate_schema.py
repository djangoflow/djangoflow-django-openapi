# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.test import Client


class Command(BaseCommand):

    def handle(self, *args, **options):
        client = Client()
        response = client.get("/api/v1/schema/")
        print(response.content.decode("utf-8"))
