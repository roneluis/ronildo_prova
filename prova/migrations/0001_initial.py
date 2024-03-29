# Generated by Django 2.2.4 on 2019-09-13 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho_De_Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(max_length=50)),
                ('peso', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=20)),
                ('carrinho_De_Compras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova.Carrinho_De_Compras')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.CharField(max_length=20)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova.Produto')),
            ],
        ),
    ]
