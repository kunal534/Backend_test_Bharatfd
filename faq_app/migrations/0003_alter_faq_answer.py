# Generated by Django 4.2.18 on 2025-02-02 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq_app', '0002_faq_answer_bn_faq_answer_hi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
    ]
