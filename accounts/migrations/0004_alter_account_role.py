# Generated by Django 4.2.3 on 2023-07-21 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_groups_alter_account_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('not_role', 'Роль не определена'), ('cashier', 'Кассир'), ('dispatcher', 'Диспетчер'), ('base', 'База')], default='not_role', max_length=10),
        ),
    ]
