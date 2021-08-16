import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from photos.models import Photo


class Command(BaseCommand):
    help = 'Loads cool pictures from Unsplash'

    def handle(self, *args, **kwargs):
        queries = ['koala', 'sloth', 'llama']
        access_token = settings.UNSPLASH_ACCESS_KEY
        page_size = 30  # Max page size

        for query in queries:
            # Load only first page of each animal.
            r = requests.get(
                f'https://api.unsplash.com/search/photos/?query={query}&per_page={page_size}&client_id={access_token}')

            photos = r.json()['results']
            print(f'Got {len(photos)} photos of {query} from Unsplash.')

            for p in photos:
                Photo.create_new(url=p['urls']['regular'], unsplash_id=p['id'])
