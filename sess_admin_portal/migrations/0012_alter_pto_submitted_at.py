# Generated by Django 5.1.6 on 2025-02-28 02:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "sess_admin_portal",
            "0011_alter_pto_options_remove_pto_date_pto_end_time_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="pto",
            name="submitted_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
