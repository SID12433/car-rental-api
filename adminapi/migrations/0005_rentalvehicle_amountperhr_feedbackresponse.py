# Generated by Django 4.2.5 on 2024-02-22 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0004_rentalvehicle_image_usedvehicle_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalvehicle',
            name='amountperhr',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.CreateModel(
            name='FeedbackResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.feedback')),
            ],
        ),
    ]
