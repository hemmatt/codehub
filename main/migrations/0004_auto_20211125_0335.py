# Generated by Django 3.2.9 on 2021-11-25 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211124_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_valid',
            field=models.CharField(blank=True, choices=[('reject', 'رد'), ('approve', 'تائید')], max_length=10, verbose_name='اعتبارسنجی'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='lang',
            field=models.CharField(choices=[('arduino', 'Arduino'), ('bash', 'Bash'), ('c', 'C'), ('cpp', 'C++'), ('csharp', 'C#'), ('css', 'CSS'), ('dart', 'Dart'), ('docker', 'DockerFile'), ('go', 'Go'), ('html', 'HTML'), ('java', 'Java'), ('js', 'JavaScript'), ('json', 'JSON'), ('lua', 'Lua'), ('md', 'markdown'), ('mysql', 'MySQL'), ('php', 'PHP'), ('python', 'Python'), ('rb', 'Ruby')], max_length=250, verbose_name='زبان برنامه\u200cنویسی'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='is_valid',
            field=models.CharField(blank=True, choices=[('reject', 'رد'), ('approve', 'تائید')], max_length=10, verbose_name='اعتبارسنجی'),
        ),
    ]
