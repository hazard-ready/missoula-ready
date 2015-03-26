# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0012_auto_20150326_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='eventOccursRecovery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+', to='world.RecoveryLevels'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='firstDayRecovery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+', to='world.RecoveryLevels'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='fourWeeksRecovery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+', to='world.RecoveryLevels'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='sevenDaysRecovery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+', to='world.RecoveryLevels'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='sixMonthsRecovery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+', to='world.RecoveryLevels'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='threeDaysRecovery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+', to='world.RecoveryLevels'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='threeMonthsRecovery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+', to='world.RecoveryLevels'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='threePlusYearsRecovery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+', to='world.RecoveryLevels'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='threeYearsRecovery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+', to='world.RecoveryLevels'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='twelveMonthsRecovery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+', to='world.RecoveryLevels'),
            preserve_default=True,
        ),
    ]
