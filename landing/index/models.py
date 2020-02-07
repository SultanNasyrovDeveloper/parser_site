from django.db import models


class IndexPage(models.Model):
    """
    Index page singleton model.
    """

    logo = models.FileField('Logo', upload_to='logo/', null=True, blank=True)
    tagline = models.CharField('Tagline', max_length=200, blank=True, null=True)
    subtagline = models.CharField('Subtagline', max_length=400, blank=True, null=True)

    about_us_tagline = models.CharField('About us tagline', max_length=100, blank=True, null=True)
    about_us_text = models.CharField('About us text', max_length=500, null=True, blank=True)
    about_us_list = models.CharField('About us list', max_length=250, null=True, blank=True, help_text='Через запятую')

    examples_header = models.CharField('Examples header', max_length=100, blank=True, null=True)

    types_header = models.CharField('Types header', max_length=100, null=True, blank=True)
    first_type_header = models.CharField('First type name', max_length=100, null=True, blank=True)
    first_type_description = models.CharField('First type description', max_length=300, null=True, blank=True)
    second_type_header = models.CharField('Second type name', max_length=100, null=True, blank=True)
    second_type_description = models.CharField('Second type name', max_length=300, null=True, blank=True)

    email = models.EmailField('Email', max_length=100, null=True, blank=True)
    phone = models.CharField('Phone number', max_length=50, null=True, blank=True)
    instagram = models.CharField('Instagram', max_length=100, null=True, blank=True)
    telegram = models.CharField('Telegram', max_length=100, null=True, blank=True)
    short_about = models.CharField('Short about', max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'Index page'
        verbose_name_plural = 'Index page'

    @classmethod
    def load(cls):
        """
        Get the only model instance.
        """
        instance, _ = cls.objects.get_or_create(id=1)
        return instance

    @property
    def about_us_list_split(self):
        """
        Get list of about us list elements.

        Returns:
            about_us_statements_list: List of about us statements.
        """
        return [statement.strip(' ,') for statement in self.about_us_list.split(', ')]

    def __str__(self) -> str:
        """
        Get string representation of current instance.
        """
        return 'Настройки страницы'



class FAQuestion(models.Model):
    """
    Frequently asked question.
    """

    question = models.CharField('Question', max_length=200)
    answer = models.TextField('Answer')

    class Meta:
        verbose_name = 'FAQuestion'

    def __str__(self):
        """
        Get string representation of the instance.
        """
        return self.question


class ParsingCategories(models.Model):
    """
    Parsing sites categories.
    """

    logo = models.FileField('Logo', upload_to='category_logos/')
    name = models.CharField('Name', max_length=50)
    description = models.CharField('Description', max_length=250)

    class Meta:
        verbose_name = 'Parsing category'
        verbose_name_plural = 'Parsing categories'

    def __str__(self):
        """
        Get instance string representation.
        """
        return self.name


class Example(models.Model):
    """
    Examples model.
    """

    file = models.FileField('File', upload_to='examples/', null=True, blank=True)
    name = models.CharField('Name', max_length=150, null=True, blank=True)
    description = models.CharField('Description', max_length=350, null=True, blank=True)

    class Meta:
        verbose_name = 'Example'
        verbose_name_plural = 'Examples'

    def __str__(self):
        """
        Get string representation if the instance.
        """
        return f'Example {self.id}'







