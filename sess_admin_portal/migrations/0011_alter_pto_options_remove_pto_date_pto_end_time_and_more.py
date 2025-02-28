# Generated by Django 5.1.6 on 2025-02-28 02:53

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sess_admin_portal", "0010_announcement"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pto",
            options={
                "ordering": ["-submitted_at"],
                "verbose_name": "PTO Request",
                "verbose_name_plural": "PTO Requests",
            },
        ),
        migrations.RemoveField(
            model_name="pto",
            name="date",
        ),
        migrations.AddField(
            model_name="pto",
            name="end_time",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pto",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pto",
            name="pto_type",
            field=models.CharField(
                choices=[
                    ("Full Day", "Full Day"),
                    ("Partial Day", "Partial Day"),
                    ("Multiple Days", "Multiple Days"),
                ],
                default="Full Day",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="pto",
            name="reviewed_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pto",
            name="reviewed_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reviewed_pto_requests",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="pto",
            name="start_time",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pto",
            name="submitted_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="pto",
            name="employee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pto_requests",
                to="sess_admin_portal.employee",
            ),
        ),
        migrations.AlterField(
            model_name="pto",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pto",
            name="start_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="pto",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="ClientReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "report_type",
                    models.CharField(
                        choices=[
                            ("Incident Report", "Client Incident Report"),
                            ("Sleep Log", "Sleep Log Report"),
                            (
                                "Individual Support Plan",
                                "Individual Support Plan (IPP)",
                            ),
                            ("Quarterly Progress Report", "Quarterly Progress Report"),
                            ("Medical Visit Summary", "Medical Visit/Hospital Summary"),
                            ("Initial Assessment", "Initial Assessment Report"),
                            ("Annual Support Plan", "Annual Support Plan Report"),
                        ],
                        max_length=50,
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("report_date", models.DateField()),
                ("content", models.JSONField()),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Draft", "Draft"),
                            ("Submitted", "Submitted"),
                            ("Approved", "Approved"),
                            ("Needs Revision", "Needs Revision"),
                        ],
                        default="Draft",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("submitted_at", models.DateTimeField(blank=True, null=True)),
                ("approved_at", models.DateTimeField(blank=True, null=True)),
                (
                    "approved_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="approved_reports",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reports",
                        to="sess_admin_portal.client",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="submitted_reports",
                        to="sess_admin_portal.employee",
                    ),
                ),
            ],
            options={
                "verbose_name": "Client Report",
                "verbose_name_plural": "Client Reports",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="EmployeeRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "request_type",
                    models.CharField(
                        choices=[
                            ("Personal Info Change", "Personal Info Change"),
                            ("Client Info Update", "Client Info Update"),
                            ("Technical Issue", "Technical Issue"),
                            ("Other", "Other"),
                        ],
                        max_length=50,
                    ),
                ),
                ("subject", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("In Progress", "In Progress"),
                            ("Resolved", "Resolved"),
                            ("Rejected", "Rejected"),
                        ],
                        default="Pending",
                        max_length=20,
                    ),
                ),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("resolved_at", models.DateTimeField(blank=True, null=True)),
                ("resolution_notes", models.TextField(blank=True, null=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="requests",
                        to="sess_admin_portal.employee",
                    ),
                ),
                (
                    "resolved_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="resolved_requests",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Employee Request",
                "verbose_name_plural": "Employee Requests",
                "ordering": ["-submitted_at"],
            },
        ),
    ]
