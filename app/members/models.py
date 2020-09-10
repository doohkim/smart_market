from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # profile_img = models.ImageField(
    #     upload_to=, blank=True, help_text='프로필 사진')
    phone = models.CharField(
        max_length=13, help_text='핸드폰 번호', blank=True)
    address = models.TextField(help_text='주소')

    # favorites = models.ManyToManyField(
    #     Keyword, through='Favorite', related_name='users', help_text='좋아요')

    class Meta:
        verbose_name = '유저'
        verbose_name_plural = '%s 목록' % verbose_name


class Favorite(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE)
    # keyword = models.ForeignKey(
    #     Keyword, related_name='favorites', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '좋아요'
        verbose_name_plural = '%s 목록' % verbose_name


class Keyword(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE)
    # keyword = models.ForeignKey(
    #     Keyword, related_name='favorites', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '키워'
        verbose_name_plural = '%s 목록' % verbose_name
