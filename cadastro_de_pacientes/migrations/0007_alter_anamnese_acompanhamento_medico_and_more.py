# Generated by Django 4.1.5 on 2024-01-23 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_de_pacientes', '0006_alter_cadastro_de_paciente_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnese',
            name='acompanhamento_medico',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='alergico',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='diabetico',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='gravidez',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='hepatite',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='hipertensao',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='hipotensao',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='hiv',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='lactante',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='problemas_circulatorios',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='teve_cancer',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='uso_medicacao',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
    ]