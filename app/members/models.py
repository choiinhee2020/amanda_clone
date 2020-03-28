from django.contrib.auth.models import AbstractUser
from django.db import models

import datetime
from config import settings


class User(AbstractUser):
    GENDER = [
        ('남자', '남자'),
        ('여자', '여자'),
    ]
    MAJOR = [
        ('건축학과', '건축학과'),
        ('교통운송학과', '교통운송학과'),
        ('기계공학과', '기계공학과'),
        ('자동차공학', '자동차공학'),
        ('산업학과', '산업학과'),
        ('광학공학', '과학공학'),
        ('전기공학', '전기공학'),
        ('전자공학', '전자공학'),
        ('응용소프트웨어공학', '응용소프트웨어공학'),
        ('토목학과', '토목학과'),
    ]
    SHAPE = [
        ('마른', '마른'),
        ('슬림탄탄', '슬림탄탄'),
        ('보통', '보통'),
        ('통통한', '통통한'),
        ('살짝볼륨', '살짝볼륨'),
        ('글래머', '글래머'),

    ]
    RESULT = [
        ('P', 'PASS'),
        ('F', 'FAIL'),
        ('Evaluate', 'Evaluate'),
        ('IMPOSSIBLE', 'IMPOSSIBLE'),
    ]
    CHARACTER = [
        ('지적인', '지적인'),
        ('차분한', '차분한'),
        ('유머있는', '유머있는'),
        ('낙천적인', '낙천적인'),
        ('내향적인', '내향적인'),
        ('외향적인', '외향적인'),
        ('감성적인', '감성적인'),
        ('상냥한', '상냥한'),
        ('귀여운', '귀여운'),
        ('섹시한', '섹시한'),
        ('4차원인', '4차원인'),
        ('발랄한', '발랄한'),
        ('도도한', '도도한'),
        ('섹시한', '토목학과'),
    ]
    username = models.CharField(max_length=100, primary_key=True, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER, max_length=10)
    password = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=20)
    average_point = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=30, blank=True)
    university = models.CharField(max_length=30, blank=True)
    major = models.CharField(max_length=30, choices=MAJOR, blank=True)
    company_name = models.CharField(max_length=10, help_text='Type company name here', blank=True)
    location = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=50, blank=True)
    body_shape = models.CharField(choices=SHAPE, max_length=10, blank=True)
    character = models.CharField(choices=CHARACTER, max_length=20, blank=True)
    date_style = models.CharField(max_length=20, blank=True)
    result = models.CharField(choices=RESULT, max_length=10, blank=True)
    status = models.BooleanField(default=False)
    chance = models.PositiveIntegerField(default=1)
    rank = models.PositiveIntegerField(default=50)
    perfection = models.PositiveIntegerField(default=50)
    birth_date = models.DateTimeField(blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    like_users = models.ManyToManyField('self', through='SendLikes', related_name='pick_me_users', symmetrical=False)
    star_users = models.ManyToManyField('self', through='SendStars', related_name='user_star_users', symmetrical=False)
    pick_users = models.ManyToManyField('self', through='SendPicks', related_name='user_pick_users', symmetrical=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        # self.age = datetime.datetime.now().year - self.birth_date.year
        if self.chance > 3:
            self.result = 'IMPOSSIBLE'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.username} 계정 생성'


class UserProfile(models.Model):
    RELIGION = [
        ('기독교', '기독교'),
        ('천주교', '천주교'),
        ('이슬람교', '이슬람교'),
        ('신천지', '신천지'),
        ('무교', '무교'),
    ]
    BLOOD = [
        ('AB', 'AB형'),
        ('A', 'A형'),
        ('B', 'B형'),
        ('O', 'O형'),
    ]
    MEDIA_CHOICES = [
        ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
         ),
        ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
         ),
        ('unknown', 'Unknown'),
    ]

    author_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, )
    religion = models.CharField(choices=RELIGION, max_length=10, blank=True)
    height = models.PositiveIntegerField(default=150)
    intro = models.CharField(max_length=500, blank=True)
    blood = models.CharField(choices=BLOOD, max_length=10, blank=True)
    smoke = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    media = models.CharField(choices=MEDIA_CHOICES, max_length=20, blank=True)
    #
    # def save(self, *args, **kwargs):
    #     self.age = datetime.datetime.now().year - self.birth_date.year
    #     super().save(*args, **kwargs)


class UserImage(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, upload_to="member/profile")


class SendLikes(models.Model):
    current_user = models.ForeignKey(User, related_name='current_user_sendlikes_set', on_delete=models.CASCADE)
    give_point = models.PositiveIntegerField(default=0)
    friend = models.ForeignKey(User, related_name='friend_sendlikes_set', on_delete=models.CASCADE)
    take_point  = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)


class SendStars(models.Model):
    current_user = models.ForeignKey(User, related_name='current_user_sendstars_set', on_delete=models.CASCADE)
    give_point = models.PositiveIntegerField(default=0)
    friend = models.ForeignKey(User, related_name='friend_sendstars_set', on_delete=models.CASCADE)
    take_point  = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)


class SendPicks(models.Model):
    current_user = models.ForeignKey(User, related_name='current_user_sendpicks_set', on_delete=models.CASCADE)
    give_point = models.PositiveIntegerField(default=0)
    friend = models.ForeignKey(User, related_name='friend_sendpicks_set', on_delete=models.CASCADE)
    take_point  = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)