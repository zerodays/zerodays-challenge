from django.db import models


class Photo(models.Model):
    # Photo url.
    url = models.TextField()
    unsplash_id = models.TextField()

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    @property
    def difference(self):
        return self.likes - self.dislikes

    @staticmethod
    def create_new(url: str, unsplash_id: str):
        photo = Photo(url=url, unsplash_id=unsplash_id)
        photo.save()
        return photo

    def add_like(self):
        self.likes += 1
        self.save()

    def add_dislike(self):
        self.dislikes += 1
        self.save()

    def to_dict(self):
        return {
            'id': self.pk,
            'unsplash_id': self.unsplash_id,
            'url': self.url,
            'likes': self.likes,
            'dislikes': self.dislikes,
            'difference': self.difference
        }
