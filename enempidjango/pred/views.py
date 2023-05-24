import joblib
from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
modelo1 = joblib.load("modelo1.joblib")

# def prever_notas(request):
#     faixa_etaria_choices = EnemScore.FAIXA_ETARIA_CHOICES
#     cor_choices = EnemScore.COR_CHOICES
#     nivel_escolaridade_mae_choices = EnemScore.NIVEL_ESCOLARIDADE_MAE_CHOICES
#     renda_choices = EnemScore.RENDA_CHOICES
#     concluiu_ensino_medio_choices = EnemScore.CONCLUIU_ENSINO_MEDIO_CHOICES

#     context = {
#         'faixa_etaria_choices': faixa_etaria_choices,
#         'cor_choices': cor_choices,
#         'nivel_escolaridade_mae_choices': nivel_escolaridade_mae_choices,
#         'renda_choices': renda_choices,
#         'concluiu_ensino_medio_choices': concluiu_ensino_medio_choices,
#     }
#     return render(request, 'pred.html', context)

# def fazer_predicao(request):
#     if request.method == 'POST':
#         # Obter os dados do formulário
#         faixa_etaria = request.POST.get('faixa_etaria')
#         cor = request.POST.get('cor')
#         nivel_escolaridade_mae = request.POST.get('nivel_escolaridade_mae')
#         renda = request.POST.get('renda')
#         concluiu_ensino_medio = request.POST.get('concluiu_ensino_medio')

#         # Criar uma nova instância de EnemScore com os dados do formulário
#         nova_instancia = EnemScore(faixa_etaria=faixa_etaria, cor=cor, nivel_escolaridade_mae=nivel_escolaridade_mae, renda=renda, concluiu_ensino_medio=concluiu_ensino_medio)

#         # Carregar o modelo salvo
#         modelo1 = joblib.load("modelo1.joblib")

#         # Fazer a predição
#         nota = modelo1.predict([nova_instancia])[0]

#         # Retornar o resultado para o usuário
#         return HttpResponse(f'A nota prevista é {nota:.2f}')

def prever_notas(request):
    faixa_etaria_choices = EnemScore.FAIXA_ETARIA_CHOICES
    cor_choices = EnemScore.COR_CHOICES
    nivel_escolaridade_mae_choices = EnemScore.NIVEL_ESCOLARIDADE_MAE_CHOICES
    renda_choices = EnemScore.RENDA_CHOICES
    concluiu_ensino_medio_choices = EnemScore.CONCLUIU_ENSINO_MEDIO_CHOICES

    context = {
        'faixa_etaria_choices': faixa_etaria_choices,
        'cor_choices': cor_choices,
        'nivel_escolaridade_mae_choices': nivel_escolaridade_mae_choices,
        'renda_choices': renda_choices,
        'concluiu_ensino_medio_choices': concluiu_ensino_medio_choices,
    }
    return render(request, 'pred.html', context)

import numpy as np

def fazer_predicao(request):
    if request.method == 'POST':
        # Obter os dados do formulário
        faixa_etaria = request.POST.get('faixa_etaria')
        cor = request.POST.get('cor')
        mae_educ = request.POST.get('mae_educ')
        renda = request.POST.get('renda')
        concluiu_ensino_medio = request.POST.get('concluiu_ensino_medio')

        # Criar uma nova instância de EnemScore com os dados do formulário
        nova_instancia = EnemScore(faixa_etaria=faixa_etaria, cor=cor, mae_educ=mae_educ, renda=renda, concluiu_ensino_medio=concluiu_ensino_medio)

        # Carregar o modelo salvo
        modelo1 = joblib.load("modelo1.joblib")

        # Fazer a predição
        instancia_array = np.array([nova_instancia.faixa_etaria, nova_instancia.cor, nova_instancia.mae_educ, nova_instancia.renda, nova_instancia.concluiu_ensino_medio])
        instancia_array = instancia_array.reshape(1, -1)
        nota = modelo1.predict(instancia_array)[0]

        # Retornar o resultado para o usuário
        return HttpResponse(f'Sua nota provável no ENEM é: {nota}')

    else:
        # Se o método da requisição não for POST, retornar uma mensagem de erro
        return HttpResponse('Método não permitido.')
    


def novoform(request):
    if request.method == 'POST':
        form = EnemForm(request.POST)
        if form.is_valid():

            dados = form.cleaned_data

            TP_SEXO = dados['TP_SEXO']
            TP_ESTADO_CIVIL = dados['TP_ESTADO_CIVIL']
            TP_ENSINO = dados['TP_ENSINO']
            TP_ANO_CONCLUIU = dados['TP_ANO_CONCLUIU']
            TP_LOCALIZACAO_ESC = dados['TP_LOCALIZACAO_ESC']
            TP_ST_CONCLUSAO = dados['TP_ST_CONCLUSAO']
            Q001 = dados['Q001']
            Q002 = dados['Q002']
            TP_ESCOLA = dados['TP_ESCOLA']
            Q003 = dados['Q003']
            Q004 = dados['Q004']
            Q005 = dados['Q005']
            Q008 = dados['Q008']
            Q006 = dados['Q006']
            Q012 = dados['Q012']
            Q022 = dados['Q022']
            Q024 = dados['Q024']
            Q025 = dados['Q025']
            TP_FAIXA_ETARIA = dados['TP_FAIXA_ETARIA']
            TP_COR_RACA = dados['TP_COR_RACA']

            dados_processados = [TP_SEXO, TP_ESTADO_CIVIL, TP_ENSINO, TP_ANO_CONCLUIU,
                                 TP_LOCALIZACAO_ESC, TP_ST_CONCLUSAO, Q001, Q002, TP_ESCOLA,
                                 Q003, Q004, Q005, Q008, Q006, Q012, Q022, Q024, Q025,
                                 TP_FAIXA_ETARIA, TP_COR_RACA]
            print(dados_processados)
            previsao = modelo1.predict([dados_processados])
            nota_matematica = previsao[0][0]
            nota_linguagens = previsao[0][1]
            nota_humanas = previsao[0][2]
            nota_natureza = previsao[0][3]
            nota_redacao = previsao[0][4]

            return render(request, 'form.html', {'form': form, 'previsao': previsao,'previsao': previsao,
        'nota_matematica': nota_matematica,
        'nota_linguagens': nota_linguagens,
        'nota_humanas': nota_humanas,
        'nota_natureza': nota_natureza,
        'nota_redacao': nota_redacao})

    else:
        form = EnemForm()
    return render(request, 'form.html', {'form': form})



