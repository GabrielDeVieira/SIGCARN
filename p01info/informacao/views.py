from contextlib import nullcontext
from datetime import date, datetime
from enum import auto
from multiprocessing import Value
from tkinter.tix import AUTO
from django.shortcuts import HttpResponse, render
import requests
import pandas as pd
import informacao
import json
from informacao.models import TbRacacor, TbInformacoes, TbSexos
from django.views import View




def inicio(request):
    return render(request, "Coleta.html")
    
    
def index(request):
    api = "https://elasticsearch-saps.saude.gov.br/desc-esus-notifica-estado-rn/_search"
    payload = json.dumps({
    "size": 10
    })

    headers = {
    'Authorization': 'Basic dXNlci1wdWJsaWMtbm90aWZpY2Fjb2VzOlphNHFOWGR5UU5TYTlZYUE=',
    'Content-Type': 'application/json'
    }

    requisicao = requests.request("GET", api, headers=headers, data=payload)
    


    try:
        lista = requisicao.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")
        
    
    
    inf = TbInformacoes.objects.all()
    rac = TbRacacor.objects.all()
    
    dicionario = {}
    #rp = pd.json_normalize(lista['hits']['hits'])
    #ff = rp[rp['_source.municipio'] =='Natal']
    for indice, valor in enumerate(lista['hits']['hits']):
        dicionario[indice] = valor
        
        
        
   
        muni = valor
        munis = str(muni)
        dic = dicionario[indice]
        dics = str(dic)
        if "'municipio': 'Natal'" in munis:
            
            if 'Assintomático' in dics:
                assintomatico = 1
            else :
                assintomatico = 0
                
            if 'Dor de Cabeça'  in dics:
                dordecabeca = 1
            else:
                dordecabeca = 0
                
            if 'Coriza' in dics:
                coriza = 1
            else:
                coriza =0
                
            if 'Tosse' in dics:
                tosse = 1
            else:
                tosse = 0
                
            if 'Febre' in dics:
                febre = 1
            else:
                febre = 0
                
            if 'Distúrbios Olfativos' in dics:
                disol = 1
            else:
                disol =0
                
            if 'Distúrbios Gustativos' in dics:
                disgust = 1
            else:
                disgust= 0
                
            if 'Dor de Garganta' in dics:
                dorgarganta = 1
            else:
                dorgarganta = 0
                
            if 'Dispneia' in dics:
                dispineia = 1
            else:
                dispineia = 0
                
            if 'Outros' in dics:
                outros =1
            else:
                outros = 0
                
            if 'Masculino' in dics :
                sexo = TbSexos.objects.get(sex_sexo='Masculino')
            elif 'Feminino' in dics:
                sexo = TbSexos.objects.get(sex_sexo='Feminino')
                
            if 'Branca' in dics:
                raco = TbRacacor.objects.get(rcc_racacor='Branca')
            elif 'Preta' in dics:
                raco =TbRacacor.objects.get(rcc_racacor='Preta')
            elif 'Parda' in dics:
                raco =TbRacacor.objects.get(rcc_racacor='Parda')
            elif 'Amarela' in dics:
                raco = TbRacacor.objects.get(rcc_racacor='Amarela')
            elif 'Indígena' in dics:
                raco = TbRacacor.objects.get(rcc_racacor='Indígena')
            elif 'Ignorado' in dics:
                raco = TbRacacor.objects.get(rcc_racacor='Ignorado')
            
            rp = pd.json_normalize(valor['_source'])
                
            idade = rp['idade'].values
            idades = str(idade)
            res = idades.translate(str.maketrans('', '', '[]'))
            
            Datasint = rp['dataInicioSintomas'].values
            Datasints = str(Datasint)
            char = "[]''"
            res1 = Datasints.translate(str.maketrans('', '', char))
            if 'None' in Datasints:
                res1 = None
                
            
            recebeuv =  rp['codigoRecebeuVacina'].values
            recebeuvs = str(recebeuv)
            res2 = recebeuvs.translate(str.maketrans('', '', "[]''"))
            
            ev = 0
            evolu =  rp['testes'].values
            if evolu:
                ecolucao = str(evolu)
                if 'Não Reagente' in ecolucao:
                    ev = 1
            else:
                ev =0
            
            rt =0
            rt1 =  rp['evolucaoCaso'].values
            rest1 = str(rt1)
            if rest1 == None:
                rt = 0
            elif 'Cancelado' in rest1:
                rt = 1
            elif 'Ignorado' in rest1:
                rt = 2
            elif 'Em tratamento' in rest1:
                rt = 3
            elif 'domiciliar' in rest1:
                rt = 4
            elif 'Internado em UT' in rest1:
                rt = 5
            elif 'Internado' in rest1:
                rt = 6
            elif 'Óbito' in rest1:
                rt = 7
            elif 'Cura' in rest1:
                rt = 8
            
            
            idapi = valor['_id']
            modid = TbInformacoes.objects.filter(inf_idapi = valor['_id'])
            idapis = str(idapi)
            modids = str(modid)
            if idapis in modids:
                idapi = 'idapi'
            else:
                info = TbInformacoes(inf_idade = res , inf_datainiciosintomas=res1, inf_idapi = idapi,
                                    inf_assintomatico = assintomatico, inf_dordecabeca= dordecabeca, inf_febre = febre,
                                    inf_dordegarganta = dorgarganta, inf_disturbiosolfativos = disol, inf_dispneia = dispineia,
                                    inf_tosse = tosse, inf_coriza = coriza, inf_disturbiosgustativos = disgust, inf_outros = outros,
                                    inf_rcc_codigo = raco, inf_sex_codigo= sexo, inf_rbv_codigo = res2, inf_evolucaoCaso = rt )
                info.save()
            
            
            contexto = {
                "infor": dicionario
            }
       
        

    return render(request, "index.html", contexto)
    
# Create your views here.

