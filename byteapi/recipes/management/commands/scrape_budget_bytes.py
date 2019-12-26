from django.core.management.base import BaseCommand

from recipes.utils.scraper import BudgetByteScraper

class Command(BaseCommand):
    help = 'Runs the Budget Bytes Web Scraper'

    def handle(self, *args, **kwargs):
        BBS = BudgetByteScraper()
        BBS.scrape_em_all()
