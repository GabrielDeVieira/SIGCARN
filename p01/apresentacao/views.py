
from datetime import date, datetime
from enum import auto
from multiprocessing import Value
from tkinter.tix import AUTO
from django.shortcuts import HttpResponse, render
import requests
import pandas as pd
import apresentacao
import json
from apresentacao.models import InformacaoTbracacor, InformacaoTbinformacoes, InformacaoTbsexos
from django.views import View





    
def index1(request):
       
    inf1 = InformacaoTbinformacoes.objects.filter(inf_rcc_codigo = 1)
    inf2 = InformacaoTbinformacoes.objects.filter(inf_rcc_codigo = 2)
    inf3 = InformacaoTbinformacoes.objects.filter(inf_rcc_codigo = 3)    
    inf4 = InformacaoTbinformacoes.objects.filter(inf_rcc_codigo = 4)
    inf5 = InformacaoTbinformacoes.objects.filter(inf_rcc_codigo = 5)
    inf6 = InformacaoTbinformacoes.objects.filter(inf_rcc_codigo = 6)
    infsex = InformacaoTbinformacoes.objects.filter(inf_sex_codigo = 1)
    infsex1 = InformacaoTbinformacoes.objects.filter(inf_sex_codigo = 2)
    infid = InformacaoTbinformacoes.objects.all()
  
    
    dicionario1 = {}
    dicionario2 = {}
    dicionario3 = {}
    dicionario4 = {}
    dicionario5 = {}
    dicionario6 = {}
    dicionarioid = {}
    dicionarios1 = {}
    dicionarios2 = {}
    dicionarios3 = {}
    dicionarios4 = {}
    dicionarios5 = {}
    dicionarios6 = {}
    dicionarios7 = {}
    dicionarios8 = {}
    dicionarios9 = {}
    dicionarios10 = {}
    dicionariosex = {}
    dicionariosex1 = {}
    dict = {}
    contexto = {}
    contrac1 = 0
    contrac2 = 0
    contrac3 = 0
    contrac4 = 0
    contrac5 = 0
    contrac6 = 0
    contid1 = 0
    contid2 = 0
    contid3 = 0
    contid4 = 0
    contassintomatico = 0
    contassintomatico1 = 0
    contcoriza = 0
    contcoriza1 = 0
    contfebre = 0
    contfebre1 = 0
    contsex = 0
    contsex1 = 0
    contdispineia = 0
    contdispineia1 = 0
    contdisgust = 0
    contdisgust1 = 0
    contdisol = 0
    contdisol1 = 0
    contdorcab = 0
    contdorcab1 = 0
    contdorg = 0
    contdorg1 = 0
    conttosse = 0
    conttosse1 = 0
    contoutros = 0
    contoutros1 = 0
    totaldecasos = 0
    
    for indice, valor in enumerate(infid):
        dict[indice] = valor
        totaldecasos = len(dict)
    
    
    #Sexo
    for indice, valor in enumerate(infsex):
        dicionariosex[indice] = valor
        
        
        contsex = len(dicionariosex)
    for indice, valor in enumerate(infsex1):
        dicionariosex1[indice] = valor
        
        
        contsex1 = len(dicionariosex1)
    #Sintomas
    for indice, valor in enumerate(infid):
        dicionarios1[indice] = valor
        if valor.inf_assintomatico == 1 :
            contassintomatico1 += 1
        elif valor.inf_assintomatico ==0:
            contassintomatico +=1
            
    for indice, valor in enumerate(infid):
        dicionarios2[indice] = valor
        if valor.inf_coriza == 1 :
            contcoriza1 += 1
        elif valor.inf_coriza ==0:
            contcoriza +=1
    
    for indice, valor in enumerate(infid):
        dicionarios3[indice] = valor
        if valor.inf_febre == 1 :
            contfebre1 += 1
        elif valor.inf_febre ==0:
            contfebre +=1     
    
    for indice, valor in enumerate(infid):
        dicionarios4[indice] = valor
        if valor.inf_dispneia == 1 :
            contdispineia1 += 1
        elif valor.inf_dispneia==0:
            contdispineia +=1   
    
    for indice, valor in enumerate(infid):
        dicionarios5[indice] = valor
        if valor.inf_disturbiosgustativos == 1 :
            contdisgust1 += 1
        elif valor.inf_disturbiosgustativos ==0:
            contdisgust +=1 
    
    for indice, valor in enumerate(infid):
        dicionarios6[indice] = valor
        if valor.inf_disturbiosolfativos == 1 :
            contdisol1 += 1
        elif valor.inf_disturbiosgustativos ==0:
            contdisol +=1  
    
    for indice, valor in enumerate(infid):
        dicionarios7[indice] = valor
        if valor.inf_dordecabeca == 1 :
            contdorcab1 += 1
        elif valor.inf_dordecabeca ==0:
            contdorcab +=1     
    
    for indice, valor in enumerate(infid):
        dicionarios8[indice] = valor
        if valor.inf_dordegarganta == 1 :
            contdorg1 += 1
        elif valor.inf_dordegarganta ==0:
            contdorg +=1
    
    for indice, valor in enumerate(infid):
        dicionarios9[indice] = valor
        if valor.inf_tosse == 1 :
            conttosse1 += 1
        elif valor.inf_tosse ==0:
            conttosse +=1
    
    for indice, valor in enumerate(infid):
        dicionarios10[indice] = valor
        if valor.inf_outros == 1 :
            contoutros1 += 1
        elif valor.inf_outros == 0:
            contoutros +=1        

    #Idade
    for indice, valor in enumerate(infid):
        dicionarioid[indice]=valor
        if valor.inf_idade > 0 and valor.inf_idade < 13:
            contid1 += 1
        elif valor.inf_idade > 12 and valor.inf_idade < 19:
            contid2 += 1
        elif valor.inf_idade > 18 and valor.inf_idade < 61:
            contid3 += 1
        elif valor.inf_idade > 60 :
            contid4 += 1
            
 #Raç/Cor 
    for indice, valor in enumerate(inf4):
        dicionario1[indice] = valor
        
        
        contrac4 = len(dicionario1)
        
    for indice, valor in enumerate(inf1):
        dicionario2[indice] = valor
        
        
        contrac1 = len(dicionario2)
    
    for indice, valor in enumerate(inf2):
        dicionario3[indice] = valor
        
        
        contrac2 = len(dicionario3)
        
    for indice, valor in enumerate(inf3):
        dicionario4[indice] = valor
        
        
        contrac3 = len(dicionario4)
        
    for indice, valor in enumerate(inf5):
        dicionario5[indice] = valor
        
        
        contrac5 = len(dicionario5)
        
    for indice, valor in enumerate(inf6):
        dicionario6[indice] = valor
        
        
        contrac6 = len(dicionario6)
        
    contexto = {
        "contrac1": contrac1,
        "contrac2": contrac2,
        "contrac3": contrac3,
        "contrac6": contrac6,
        "contrac5": contrac5,
        "contrac4": contrac4,
        "contid1": contid1,
        "contid2": contid2,
        "contid3": contid3,
        "contid4": contid4,
        "contassintomatico": contassintomatico,
        "contassintomatico1": contassintomatico1,
        "contcoriza1": contcoriza1,
        "contcoriza": contcoriza,
        "contsex" : contsex,
        "contsex1" : contsex1,
        "contfebre": contfebre,
        "contfebre1": contfebre1,
        "contdispineia": contdispineia,
        "contdispineia1": contdispineia1,
        "contdisgust" : contdisgust,
        "contdisgust1" : contdisgust1,
        "contdisol" : contdisol,
        "contdisol1" : contdisol1,
        "contdorcab" : contdorcab,
        "contdorcab1" : contdorcab1,
        "contdorg": contdorg,
        "contdorg1": contdorg1,
        "conttosse": conttosse,
        "conttosse1": conttosse1,
        "contoutros": contoutros,
        "contoutros1": contoutros1,
        "totaldecasos" : totaldecasos
    }
   
       
    
       
       
    
    return render(request, "index1.html", contexto)
def valor():
    
    return 40
# Create your views here.

