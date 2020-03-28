# Generated by Django 2.2.11 on 2020-03-28 02:20

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('남자', '남자'), ('여자', '여자')], max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField(default=20)),
                ('average_point', models.PositiveIntegerField(default=0)),
                ('job', models.CharField(blank=True, max_length=30)),
                ('university', models.CharField(blank=True, max_length=30)),
                ('major', models.CharField(blank=True, choices=[('건축학과', '건축학과'), ('교통운송학과', '교통운송학과'), ('기계공학과', '기계공학과'), ('자동차공학', '자동차공학'), ('산업학과', '산업학과'), ('광학공학', '과학공학'), ('전기공학', '전기공학'), ('전자공학', '전자공학'), ('응용소프트웨어공학', '응용소프트웨어공학'), ('토목학과', '토목학과')], max_length=30)),
                ('company_name', models.CharField(blank=True, help_text='Type company name here', max_length=10)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('body_shape', models.CharField(blank=True, choices=[('마른', '마른'), ('슬림탄탄', '슬림탄탄'), ('보통', '보통'), ('통통한', '통통한'), ('살짝볼륨', '살짝볼륨'), ('글래머', '글래머')], max_length=10)),
                ('character', models.CharField(blank=True, choices=[('지적인', '지적인'), ('차분한', '차분한'), ('유머있는', '유머있는'), ('낙천적인', '낙천적인'), ('내향적인', '내향적인'), ('외향적인', '외향적인'), ('감성적인', '감성적인'), ('상냥한', '상냥한'), ('귀여운', '귀여운'), ('섹시한', '섹시한'), ('4차원인', '4차원인'), ('발랄한', '발랄한'), ('도도한', '도도한'), ('섹시한', '토목학과')], max_length=20)),
                ('date_style', models.CharField(blank=True, max_length=20)),
                ('result', models.CharField(blank=True, choices=[('P', 'PASS'), ('F', 'FAIL'), ('Evaluate', 'Evaluate'), ('IMPOSSIBLE', 'IMPOSSIBLE')], max_length=10)),
                ('status', models.BooleanField(default=False)),
                ('chance', models.PositiveIntegerField(default=1)),
                ('rank', models.PositiveIntegerField(default=50)),
                ('perfection', models.PositiveIntegerField(default=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('author_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('religion', models.CharField(blank=True, choices=[('기독교', '기독교'), ('천주교', '천주교'), ('이슬람교', '이슬람교'), ('신천지', '신천지'), ('무교', '무교')], max_length=10)),
                ('height', models.PositiveIntegerField(default=150)),
                ('intro', models.CharField(blank=True, max_length=500)),
                ('blood', models.CharField(blank=True, choices=[('AB', 'AB형'), ('A', 'A형'), ('B', 'B형'), ('O', 'O형')], max_length=10)),
                ('smoke', models.BooleanField(default=False)),
                ('alcohol', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, upload_to='member/profile')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SendStars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('give_point', models.PositiveIntegerField(default=0)),
                ('take_point', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('current_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_user_sendstars_set', to=settings.AUTH_USER_MODEL)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_sendstars_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SendPicks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('give_point', models.PositiveIntegerField(default=0)),
                ('take_point', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('current_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_user_sendpicks_set', to=settings.AUTH_USER_MODEL)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_sendpicks_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SendLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('give_point', models.PositiveIntegerField(default=0)),
                ('take_point', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('current_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_user_sendlikes_set', to=settings.AUTH_USER_MODEL)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_sendlikes_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='like_users',
            field=models.ManyToManyField(related_name='pick_me_users', through='members.SendLikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='pick_users',
            field=models.ManyToManyField(related_name='user_pick_users', through='members.SendPicks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='star_users',
            field=models.ManyToManyField(related_name='user_star_users', through='members.SendStars', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
