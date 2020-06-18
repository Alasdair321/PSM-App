from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
import os
import time

fs = FileSystemStorage(location='D:\\storage')

class Media(models.Model):
    """
    Model representing a media item which will appear on the profile feed.
    Examples:
        Video, Image, Audio, Text
    """

    media_types = [
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('image', 'Image'),
    ]

    date = models.DateField(null=False, default=timezone.now)
    media_type = models.CharField(
        max_length=5,
        choices=media_types,
        default='text',
        help_text='The type of media',
        blank=False,
    )
    message = models.TextField(
        null=True,
        blank=True,
        help_text='Message or media caption'
    )
    served_file = models.FileField(upload_to=os.path.join(time.strftime('%Y%m%d%H%M%S', time.gmtime())), null=True, blank=True)
    raw_file = models.FileField(upload_to=os.path.join('raw', time.strftime('%Y%m%d%H%M%S', time.gmtime())), null=True, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('content-detail', args=[str(self.id)])
