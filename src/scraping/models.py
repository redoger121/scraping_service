from django.db import models

# Create your models here.


class City(models.Model):
    name=models.CharField(max_length=50, verbose_name= 'Название', unique=True)
    slug=models.SlugField(max_length=50, blank=True, unique=True)


    class Meta:
        verbose_name='Город'
        verbose_name_plural='Города'

    def __str__(self):
        return self.name




class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Язык программирования', unique=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    url=models.URLField(unique=True)
    title=models.CharField(max_length=250, verbose_name='Заголовок вакансии')
    company=models.CharField(max_length=250, verbose_name='Компания')
    description=models.TextField(verbose_name='Описание вакансии')
    city=models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    language=models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Язык программирования')
    timestamp=models.DateField(auto_now_add=True )


    class Meta:
        verbose_name='Вакансия'
        verbose_name_plural='Вакансии'

    def __str__(self):
        return self.title


