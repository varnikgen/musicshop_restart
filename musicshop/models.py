from django.db import models


class MediaType(models.Model):
    """Мелдианоситель"""

    name = models.CharField(max_length=100, verbose_name="Название медианосителя")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Медианоситель'
        verbose_name_plural = 'Медианосители'


class Member(models.Model):
    """Музыкант"""

    name = models.CharField(max_length=255, verbose_name="Имя музыканта")
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Музыкант'
        verbose_name_plural = 'Музыканты'


class Genre(models.Model):
    """Музыкальный жанр"""

    name = models.CharField(max_length=50, verbose_name='Название жанра')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Artist(models.Model):
    """Исполнитель"""

    name = models.CharField(max_length=255, verbose_name="Исполнитель/группа")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    members = models.ManyToManyField(Member, verbose_name="Участник", related_name="artist")
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name} | {self.genre.name}'
    
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Album(models.Model):
    """Альбом исполнителя"""

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="Исполнитель")
    name = models.CharField(max_length=255, verbose_name="Название альбома")
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE, verbose_name="Носитель")
    song_list = models.TextField(verbose_name="Трэклист")
    release_date = models.DateField(verbose_name="Дата релиза")
    slug = models.SlugField()
    description = models.TextField(verbose_name="Описание", )

    def __str__(self):
        return self.name
    
