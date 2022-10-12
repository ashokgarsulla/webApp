from django.db.models.signals import post_delete
from django.core.files.storage import default_storage
from django.dispatch import receiver
from app.models import Post

@receiver(post_delete, sender=Post)
def delete_associated_files(sender, instance, **kwargs):
    """Remove all files of an image after deletion."""
    path = instance.file.name
    print(path)
    if path:
        default_storage.delete(path)