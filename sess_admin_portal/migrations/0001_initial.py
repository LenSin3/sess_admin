# Generated by Django 5.1.6 on 2025-03-01 22:12

import django.db.models.deletion
import smart_selects.db_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "category",
                    models.CharField(
                        choices=[
                            ("Physical", "Physical"),
                            ("Intellectual", "Intellectual"),
                            ("Physical/Intellectual", "Physical/Intellectual"),
                        ],
                        default="Physical",
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Medication",
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
                ("medication", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(max_length=255)),
                (
                    "apt_or_unit",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("zipcode", models.CharField(max_length=10)),
                ("object_id", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Announcement",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("date_posted", models.DateTimeField(auto_now_add=True)),
                (
                    "expiry_date",
                    models.DateField(
                        blank=True,
                        help_text="Leave blank if announcement doesn't expire",
                        null=True,
                    ),
                ),
                (
                    "important",
                    models.BooleanField(
                        default=False,
                        help_text="Important announcements are highlighted",
                    ),
                ),
                (
                    "announcement_type",
                    models.CharField(
                        choices=[
                            ("general", "General"),
                            ("policy", "Policy Update"),
                            ("event", "Event"),
                            ("holiday", "Holiday"),
                        ],
                        default="general",
                        max_length=20,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="announcements/"
                    ),
                ),
                (
                    "posted_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="announcements",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-date_posted"],
            },
        ),
        migrations.CreateModel(
            name="Client",
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
                ("first_name", models.CharField(max_length=100)),
                (
                    "middle_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("last_name", models.CharField(max_length=100)),
                (
                    "sex",
                    models.CharField(
                        choices=[("Male", "M"), ("Female", "F")],
                        default="Male",
                        max_length=100,
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                ("date_of_birth", models.DateField()),
                ("onboarding_date", models.DateField()),
                ("offboarding_date", models.DateField(blank=True, null=True)),
                ("active", models.BooleanField()),
                (
                    "address",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.address",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Appointment",
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
                ("appointment_date", models.DateField()),
                ("appointment_time", models.TimeField()),
                ("appointment_location", models.CharField(max_length=100)),
                ("appointment_reason", models.TextField()),
                ("status", models.CharField(max_length=100)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.client",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClientFamily",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                (
                    "relationship",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.client",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Diagnosis",
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
                ("diagnosis", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("first_name", models.CharField(max_length=100)),
                (
                    "middle_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("last_name", models.CharField(max_length=100)),
                (
                    "sex",
                    models.CharField(
                        choices=[("Male", "M"), ("Female", "F")],
                        default="Male",
                        max_length=100,
                    ),
                ),
                ("phone_number", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("date_of_birth", models.DateField()),
                ("hire_date", models.DateField()),
                ("termination_date", models.DateField(blank=True, null=True)),
                ("active", models.BooleanField()),
                ("role", models.CharField(max_length=100)),
                (
                    "address",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.address",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.client",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employee",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DailyReport",
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
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("report", models.TextField()),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.client",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.employee",
                    ),
                ),
            ],
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
        migrations.CreateModel(
            name="ExternalCareTeam",
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
                ("first_name", models.CharField(blank=True, max_length=100, null=True)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                ("role", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "address",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.address",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MedicalHistory",
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
                ("date", models.DateField()),
                ("doctors_notes", models.TextField(blank=True, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.category",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.client",
                    ),
                ),
                (
                    "diagnosis",
                    smart_selects.db_fields.ChainedForeignKey(
                        auto_choose=True,
                        chained_field="category",
                        chained_model_field="category",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.diagnosis",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MedicationRegimen",
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
                ("dosage", models.CharField(max_length=100)),
                ("frequency", models.CharField(max_length=100)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.client",
                    ),
                ),
                (
                    "medication",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.medication",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProfilePicture",
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
                ("image", models.ImageField(upload_to="profile_pics/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                ("object_id", models.PositiveIntegerField()),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Program",
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
                ("program", models.CharField(max_length=100)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                (
                    "address",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.address",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClientProgram",
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
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.client",
                    ),
                ),
                (
                    "program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.program",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PTO",
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
                    "pto_type",
                    models.CharField(
                        choices=[
                            ("Full Day", "Full Day"),
                            ("Partial Day", "Partial Day"),
                            ("Multiple Days", "Multiple Days"),
                        ],
                        default="Full Day",
                        max_length=20,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("start_time", models.TimeField(blank=True, null=True)),
                ("end_time", models.TimeField(blank=True, null=True)),
                ("reason", models.TextField(blank=True, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Rejected", "Rejected"),
                        ],
                        default="Pending",
                        max_length=20,
                    ),
                ),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("reviewed_at", models.DateTimeField(blank=True, null=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pto_requests",
                        to="sess_admin_portal.employee",
                    ),
                ),
                (
                    "reviewed_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="reviewed_pto_requests",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "PTO Request",
                "verbose_name_plural": "PTO Requests",
                "ordering": ["-submitted_at"],
            },
        ),
        migrations.CreateModel(
            name="RegionalCenter",
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
                ("regional_center", models.CharField(max_length=100)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                (
                    "address",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.address",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="employee",
            name="regionalCenter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="sess_admin_portal.regionalcenter",
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="regional_center",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="sess_admin_portal.regionalcenter",
            ),
        ),
        migrations.CreateModel(
            name="TimesheetSubmission",
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
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Rejected", "Rejected"),
                        ],
                        default="Pending",
                        max_length=20,
                    ),
                ),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.employee",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Timesheet",
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
                ("date", models.DateField()),
                ("time_in", models.TimeField()),
                ("time_out", models.TimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Rejected", "Rejected"),
                        ],
                        default="Pending",
                        max_length=20,
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sess_admin_portal.employee",
                    ),
                ),
                (
                    "submission",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timesheets",
                        to="sess_admin_portal.timesheetsubmission",
                    ),
                ),
            ],
        ),
    ]
