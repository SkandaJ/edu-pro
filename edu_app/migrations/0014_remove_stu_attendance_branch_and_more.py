# Generated by Django 4.1 on 2023-09-01 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "edu_app",
            "0013_stu_attendance_attendance_alter_stu_attendance_date_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="stu_attendance", name="Branch",),
        migrations.RemoveField(model_name="stu_attendance", name="attendance",),
        migrations.RemoveField(model_name="stu_attendance", name="ending_time",),
        migrations.RemoveField(model_name="stu_attendance", name="semester",),
        migrations.RemoveField(model_name="stu_attendance", name="starting_time",),
        migrations.RemoveField(model_name="stu_attendance", name="subject_code",),
        migrations.RemoveField(model_name="stu_attendance", name="usn",),
        migrations.AddField(
            model_name="stu_attendance",
            name="end_time",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="stu_attendance",
            name="is_present",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="stu_attendance",
            name="start_time",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="stu_attendance",
            name="student_name",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="edu_app.students",
            ),
        ),
        migrations.AddField(
            model_name="stu_attendance",
            name="subject",
            field=models.CharField(default="None", max_length=50),
        ),
        migrations.AlterField(
            model_name="stu_attendance",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="students",
            name="semester",
            field=models.CharField(default="0", max_length=2),
        ),
    ]
