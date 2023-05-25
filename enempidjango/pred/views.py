import joblib
from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
import numpy as np
modelo1 = joblib.load("modelo1.joblib")


def home(request):
    return render(request, 'home.html')

def prediction(request):
    if request.method == 'POST':
        form = EnemForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data

            print(dados)
            TP_FAIXA_ETARIA = dados['TP_FAIXA_ETARIA']
            TP_COR_RACA = dados['TP_COR_RACA']
            TP_SEXO_MASCULINO = dados['TP_SEXO_MASCULINO']
            TP_ESTADO_CIVIL = dados['TP_ESTADO_CIVIL']
            TP_ENSINO = dados['TP_ENSINO']
            TP_ANO_CONCLUIU = dados['TP_ANO_CONCLUIU']
            TP_LOCALIZACAO_ESC = dados['TP_LOCALIZACAO_ESC']
            TP_ST_CONCLUSAO = dados['TP_ST_CONCLUSAO']
            TP_ESCOLA = dados['TP_ESCOLA']
            Q001 = dados['Q001']
            Q002 = dados['Q002']
            Q003 = dados['Q003']
            Q004 = dados['Q004']
            Q005 = dados['Q005']
            Q008 = dados['Q008']
            Q006 = dados['Q006']
            Q012 = dados['Q012']
            Q022 = dados['Q022']
            Q024 = dados['Q024']
            Q025 = dados['Q025']

            dados_processados = [TP_SEXO_MASCULINO, TP_ESTADO_CIVIL, TP_ENSINO, TP_ANO_CONCLUIU,
                                 TP_LOCALIZACAO_ESC, TP_ST_CONCLUSAO, Q001, Q002, TP_ESCOLA,
                                 Q003, Q004, Q005, Q008, Q006, Q012, Q022, Q024, Q025,
                                 TP_FAIXA_ETARIA, TP_COR_RACA]

           
            previsao = modelo1.predict([dados_processados])

            nota_matematica = previsao[0][0]
            nota_linguagens = previsao[0][1]
            nota_humanas = previsao[0][2]
            nota_natureza = previsao[0][3]
            nota_redacao = previsao[0][4]

            return render(request,  'prediction.html', {'form': form, 'nota_matematica': nota_matematica,'nota_linguagens': nota_linguagens,'nota_humanas': nota_humanas,'nota_natureza': nota_natureza,'nota_redacao': nota_redacao})

    else:
        form = EnemForm()
    return render(request, 'prediction.html', {'form': form})






