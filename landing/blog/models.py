from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    """
    Post model.
    """

    image = models.ImageField('Image', upload_to='post_images/')
    name = models.CharField('Name', max_length=500)
    body = RichTextField('Body')

    created = models.DateTimeField('Created', auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        ordering = ('created', )


    def __str__(self):
        """
        Get string representation of the instance.
        """
        return self.name if self.name else f'Post {self.id}'

    def get_absolute_url(self) -> str:
        return reverse('blog:detail', args=(self.id, ))

