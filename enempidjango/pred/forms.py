from django.forms import ModelForm
from .models import *

class EnemForm(ModelForm):
    class Meta:
        model = EnemScore
        fields = '__all__'
        labels = {
            'TP_FAIXA_ETARIA':'Faixa Etária',
            'TP_SEXO_MASCULINO': 'Sexo',
            'TP_ESTADO_CIVIL': 'Estado Civil',
            'TP_COR_RACA': 'Cor/Raça',
            'TP_ST_CONCLUSAO': 'Situação de conclusão do Ensino Médio',
            'TP_ANO_CONCLUIU': 'Ano de Conclusão do Ensino Médio',
            'TP_ESCOLA': 'Tipo de escola do Ensino Médio',
            'TP_ENSINO': 'Tipo de instituição que concluiu ou concluirá o Ensino Médio',
            'TP_LOCALIZACAO_ESC': 'Localização (Escola)',
            'Q001': 'Até que série seu pai, ou o homem responsável por você, estudou?',
            'Q002': 'Até que série sua mãe, ou a mulher responsável por você, estudou?',
            'Q003': 'Ocupação do seu pai ou homem responsável por você. (Escolher a mais próxima)',
            'Q004': 'Ocupação da sua mãe ou mulher responsável por você. (Escolher a mais próxima)',
            'Q005': 'Incluindo você, quantas pessoas moram atualmente em sua residência?',
            'Q006': 'Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)',
            'Q008': 'Na sua residência tem banheiro?',
            'Q012': 'Na sua residência tem geladeira?',
            'Q022': 'Na sua residência tem telefone celular?',
            'Q024': 'Na sua residência tem computador?',
            'Q025': 'Na sua residência tem acesso à Internet?'
            }