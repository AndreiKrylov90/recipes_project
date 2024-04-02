from django.core.management.base import BaseCommand
from recipes.models import Category


class Command(BaseCommand):
    help = 'Load initial categories into the database'

    def handle(self, *args, **kwargs):
        categories = ['Русская кухня', 'Домашние блюда', 'Итальянская кухня', 'Грузинская кухня', 'Французская кухня']

        for category_name in categories:
            Category.objects.get_or_create(name=category_name)

        self.stdout.write(self.style.SUCCESS('Categories have been loaded successfully'))
