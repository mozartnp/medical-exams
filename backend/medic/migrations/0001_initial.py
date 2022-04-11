# Generated by Django 4.0.4 on 2022-04-11 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medic',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(choices=[(1, 'Alergia e Imunologia'), (2, 'Anestesiologia'), (3, 'Angiologia'), (4, 'Cardiologia'), (5, 'Cirurgia Cardiovascular'), (6, 'Cirurgia da Mão'), (7, 'Cirurgia de cabeça e pescoço'), (8, 'Cirurgia do Aparelho Digestivo'), (9, 'Cirurgia Geral'), (10, 'Cirurgia Pediátrica'), (11, 'Cirurgia Plástica'), (12, 'Cirurgia Torácica'), (13, 'Cirurgia Vascular'), (14, 'Clínica Médica'), (15, 'Coloproctologia'), (16, 'Dermatologia'), (17, 'Endocrinologia e Metabologia'), (18, 'Endoscopia'), (19, 'Gastroenterologia'), (20, 'Genética médica'), (21, 'Geriatria'), (22, 'Ginecologia e obstetrícia'), (23, 'Hematologia e Hemoterapia'), (24, 'Homeopatia'), (25, 'Infectologia'), (26, 'Mastologia'), (27, 'Medicina de Família e Comunidade'), (
                    28, 'Medicina de Emergência'), (29, 'Medicina do Trabalho'), (30, 'Medicina do Tráfego'), (31, 'Medicina Esportiva'), (32, 'Medicina Física e Reabilitação'), (33, 'Medicina Intensiva'), (34, 'Medicina Legal e Perícia Médica'), (35, 'Medicina Nuclear'), (36, 'Medicina Preventiva e Social'), (37, 'Nefrologia'), (38, 'Neurocirurgia'), (39, 'Neurologia'), (40, 'Nutrologia'), (41, 'Obstetrícia'), (42, 'Oftalmologia'), (43, 'Ortopedia e Traumatologia'), (44, 'Otorrinolaringologia'), (45, 'Patologia'), (46, 'Patologia Clínica/Medicina laboratorial'), (47, 'Pediatria'), (48, 'Pneumologia'), (49, 'Psiquiatria'), (50, 'Radiologia e Diagnóstico por Imagem'), (51, 'Radioterapia'), (52, 'Reumatologia'), (53, 'Toxicologia médica'), (54, 'Urologia')], max_length=3)),
                ('price_consultation', models.DecimalField(
                    decimal_places=2, max_digits=8)),
            ],
        ),
    ]
