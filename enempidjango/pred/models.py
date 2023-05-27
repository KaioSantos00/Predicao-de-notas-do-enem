from django.db import models

# Create your models here.
from django.db import models

class EnemScore(models.Model):
    FAIXA_ETARIA_CHOICES = (
        (1, 'Menor de 17 anos'),
        (2, '17 anos'),
        (3, '18 anos'),
        (4, '19 anos'),
        (5, '20 anos'),
        (6, '21 anos'),
        (7, '22 anos'),
        (8, '23 anos'),
        (9, '24 anos'),
        (10, '25 anos'),
        (11, 'Entre 26 e 30 anos'),
        (12, 'Entre 31 e 35 anos'),
        (13, 'Entre 36 e 40 anos'),
        (14, 'Entre 41 e 45 anos'),
        (15, 'Entre 46 e 50 anos'),
        (16, 'Entre 51 e 55 anos'),
        (17, 'Entre 56 e 60 anos'),
        (18, 'Entre 61 e 65 anos'),
        (19, 'Entre 66 e 70 anos'),
        (20, 'Maior de 70 anos')
    )
    COR_CHOICES = [
        (0, 'Não declarado'),
        (1, 'Branca'),
        (2, 'Preta'),
        (3, 'Parda'),
        (4, 'Amarela'),
        (5, 'Indígena')
    ]
    
    NIVEL_ESCOLARIDADE_MAE_CHOICES = [
    (1, 'Nunca estudou'),
    (2, 'Não completou a 4ª série/5º ano do Ensino Fundamental'),
    (3, 'Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental'),
    (4, 'Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio'),
    (5, 'Completou o Ensino Médio, mas não completou a Faculdade'),
    (6, 'Completou a Faculdade, mas não completou a Pós-graduação'),
    (7, 'Completou a Pós-graduação'),
    (8, 'Não sei')
]

    RENDA_CHOICES = [    (1, 'Nenhuma Renda'),    (2, 'Até R$ 1.045,00'),    
                     (3, 'De R$ 1.045,01 até R$ 1.567,50'),    (4, 'De R$ 1.567,51 até R$ 2.090,00'),    
                     (5, 'De R$ 2.090,01 até R$ 2.612,50'),    (6, 'De R$ 2.612,51 até R$ 3.135,00'),    
                     (6, 'De R$ 3.135,01 até R$ 4.180,00'),    (8, 'De R$ 4.180,01 até R$ 5.225,00'),    
                     (9, 'De R$ 5.225,01 até R$ 6.270,00'),    (10, 'De R$ 6.270,01 até R$ 7.315,00'),    
                     (11, 'De R$ 7.315,01 até R$ 8.360,00'),    (12, 'De R$ 8.360,01 até R$ 9.405,00'),    
                     (13, 'De R$ 9.405,01 até R$ 10.450,00'),    (14, 'De R$ 10.450,01 até R$ 12.540,00'),    
                     (15, 'De R$ 12.540,01 até R$ 15.675,00'),    (16, 'De R$ 15.675,01 até R$ 20.900,00'),    
                     (17, 'Acima de R$ 20.900,00')]
    
    CONCLUIU_ENSINO_MEDIO_CHOICES = [
        (1, 'Já concluí o Ensino Médio'),
        (2, 'Estou cursando e concluirei o Ensino Médio em 2020'),
        (3, 'Estou cursando e concluirei o Ensino Médio após 2020'),
        (4, 'Não concluí e não estou cursando o Ensino Médio')
    ]
    LOCAL_CHOICES = [
        (1, 'Urbana'),(2,'Rural')
    ]
    ANO_CONCLUIU_CHOICES = [
        (0,	'Não informado'),
        (1,	'2019'),
        (2,	'2018'),
        (3,	'2017'),
        (4,'2016'),
        (5,	'2015'),
        (6,	'2014'),
        (7,	'2013'),
        (8,	'2012'),
        (9,	'2011'),
        (10,'2010'),
        (11,'2009'),
        (12	,'2008'),
        (13	,'2007'),
        (14	,'Antes de 2007')
    ]
    ENSINO_CHOICES = [
        (1	,'Ensino Regular'),
    (2	,'Educação Especial - Modalidade Substitutiva'),
    (3	,'Educação de Jovens e Adultos')
    ]
    OCUPACAO_PAI_CHOICES = [
       (1, 'Lavrador, agricultor sem empregados, bóia fria, criador de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultor, pescador, lenhador, seringueiro, extrativista.'),
    (2, 'Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro (em casas particulares), motorista particular, jardineiro, faxineiro de empresas e prédios, vigilante, porteiro, carteiro, office-boy, vendedor, caixa, atendente de loja, auxiliar administrativo, recepcionista, servente de pedreiro, repositor de mercadoria.'),
    (3,	'Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro, joalheiro, torneiro mecânico, operador de máquinas, soldador, operário de fábrica, trabalhador da mineração, pedreiro, pintor, eletricista, encanador, motorista, caminhoneiro, taxista.'),
    (4,	'Professor (de ensino fundamental ou médio, idioma, música, artes etc.), técnico (de enfermagem, contabilidade, eletrônica etc.), policial, militar de baixa patente (soldado, cabo, sargento), corretor de imóveis, supervisor, gerente, mestre de obras, pastor, microempresário (proprietário de empresa com menos de 10 empregados), pequeno comerciante, pequeno proprietário de terras, trabalhador autônomo ou por conta própria.'),
    (5,	'Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel, professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados.')
    ]
    OCUPACAO_MAE_CHOICES = [
       (1, 'Lavrador, agricultor sem empregados, bóia fria, criador de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultor, pescador, lenhador, seringueiro, extrativista.'),
    (2, 'Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro (em casas particulares), motorista particular, jardineiro, faxineiro de empresas e prédios, vigilante, porteiro, carteiro, office-boy, vendedor, caixa, atendente de loja, auxiliar administrativo, recepcionista, servente de pedreiro, repositor de mercadoria.'),
    (3,	'Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro, joalheiro, torneiro mecânico, operador de máquinas, soldador, operário de fábrica, trabalhador da mineração, pedreiro, pintor, eletricista, encanador, motorista, caminhoneiro, taxista.'),
    (4,	'Professor (de ensino fundamental ou médio, idioma, música, artes etc.), técnico (de enfermagem, contabilidade, eletrônica etc.), policial, militar de baixa patente (soldado, cabo, sargento), corretor de imóveis, supervisor, gerente, mestre de obras, pastor, microempresário (proprietário de empresa com menos de 10 empregados), pequeno comerciante, pequeno proprietário de terras, trabalhador autônomo ou por conta própria.'),
    (5,	'Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel, professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados.')
    ]
    Q05_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20')
    ]

    Q08_CHOICES = [
        (1, 'Não'),
        (2, 'Sim, um'),
        (3, 'Sim, dos'),
        (4, 'Sim, tres'),
        (5, 'Sim, quatro ou mais')
    ]
    GELADEIRA_CHOICES = [
       (1,	'Não'),
        (2,	'Sim, uma.'),
        (3,	'Sim, duas.'),
        (4,	'Sim, três.'),
        (5,	'Sim, quatro ou mais.')
    ]
    TELEFONE_CHOICES = [
       (1,	'Não.'),
        (2,	'Sim, um.'),
        (3,	'Sim, dois.'),
        (4,	'Sim, três.'),
        (5,	'Sim, quatro ou mais.')
    ]
    Q024_CHOICES = [
        (1, 'Não'),
        (2, 'Sim, um'),
        (3, 'Sim, dos'),
        (4, 'Sim, tres'),
        (5, 'Sim, quatro ou mais')

    ]
    TP_ESCOLA_CHOICES = [
        (1, 'Não respondeu'),
        (2, 'Pública'),
        (3, 'Privada'),
        (4, 'Exterior')
    ]
    ESTADO_CIVIL_CHOICES = [
        (1, 'Solteiro'),
        (2, 'Casado'),
        (3, 'Divorciado'),
        (4, 'Separado'),
        (5, 'Viuvo')
    ]
    NIVEL_ESCOLARIDADE_PAI_CHOICES = [
    (1, 'Nunca estudou'),
    (2, 'Não completou a 4ª série/5º ano do Ensino Fundamental'),
    (3, 'Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental'),
    (4, 'Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio'),
    (5, 'Completou o Ensino Médio, mas não completou a Faculdade'),
    (6, 'Completou a Faculdade, mas não completou a Pós-graduação'),
    (7, 'Completou a Pós-graduação'),
    (8, 'Não sei')
    ]   
    SEXO_CHOICES = [
        (1,'Masculino'),(2,'Feminino'),
    ]
    Q025_CHOICES = [
        (1,'Não'),
        (2,'Sim'),

    ]
    TP_FAIXA_ETARIA = models.IntegerField(choices=FAIXA_ETARIA_CHOICES, max_length=20)
    TP_SEXO_MASCULINO = models.IntegerField(choices=SEXO_CHOICES)
    TP_ESTADO_CIVIL = models.IntegerField(choices=ESTADO_CIVIL_CHOICES, max_length=20)
    TP_COR_RACA = models.IntegerField(max_length=20, choices=COR_CHOICES)
    TP_ST_CONCLUSAO = models.IntegerField(choices=CONCLUIU_ENSINO_MEDIO_CHOICES)
    TP_ANO_CONCLUIU = models.IntegerField(max_length=300, choices=ANO_CONCLUIU_CHOICES)
    TP_ESCOLA = models.IntegerField(choices=TP_ESCOLA_CHOICES, max_length=20)
    TP_ENSINO =  models.IntegerField(max_length=300, choices=ENSINO_CHOICES)
    TP_LOCALIZACAO_ESC = models.IntegerField(max_length=300, choices=LOCAL_CHOICES)
    Q001 = models.IntegerField(max_length=300, choices=NIVEL_ESCOLARIDADE_PAI_CHOICES)
    Q002 = models.IntegerField(max_length=300, choices=NIVEL_ESCOLARIDADE_MAE_CHOICES)
    Q003 = models.IntegerField(max_length=300, choices=OCUPACAO_PAI_CHOICES)
    Q004 = models.IntegerField(max_length=300, choices=OCUPACAO_MAE_CHOICES)
    Q005 = models.IntegerField(choices=Q05_CHOICES, max_length=20)
    Q008 = models.IntegerField(choices=Q08_CHOICES, max_length=20)
    Q006 = models.IntegerField(max_length=30, choices=RENDA_CHOICES)
    Q012= models.IntegerField(max_length=30, choices=GELADEIRA_CHOICES)
    Q022= models.IntegerField(max_length=30, choices=TELEFONE_CHOICES)
    Q024 = models.IntegerField(choices=Q024_CHOICES, max_length=20)
    Q025 = models.IntegerField(choices=Q025_CHOICES, max_length=20)
    def __str__(self):
        return f"EnemScore object ({self.renda})"
