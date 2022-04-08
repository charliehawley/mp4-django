from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wisecrack', '0019_auto_20220407_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub',
            name='prompt',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wisecrack.prompt'),
        ),
    ]
