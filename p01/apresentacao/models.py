from django.db import models


class InformacaoTbracacor(models.Model):
    rcc_codigo = models.IntegerField(primary_key=True)
    rcc_racacor = models.CharField(max_length=10, blank=True, null=True)
    def __str__ (self):
         return self.rcc_racacor

    class Meta:
        managed = False
        db_table = 'informacao_tbracacor'


class InformacaoTbsexos(models.Model):
    sex_codigo = models.IntegerField(primary_key=True)
    sex_sexo = models.CharField(max_length=20, blank=True, null=True)
    def __str__ (self):
         return self.sex_sexo
    

    class Meta:
        managed = False
        db_table = 'informacao_tbsexos'

class InformacaoTbinformacoes(models.Model):
    inf_codigo = models.AutoField(primary_key=True)
    inf_idade = models.IntegerField(blank=True, null=True)
    inf_datainiciosintomas = models.DateTimeField(blank=True, null=True)
    inf_assintomatico = models.IntegerField(blank=True, null=True)
    inf_dordecabeca = models.IntegerField(blank=True, null=True)
    inf_febre = models.IntegerField(blank=True, null=True)
    inf_disturbiosgustativos = models.IntegerField(blank=True, null=True)
    inf_dordegarganta = models.IntegerField(blank=True, null=True)
    inf_disturbiosolfativos = models.IntegerField(blank=True, null=True)
    inf_dispneia = models.IntegerField(blank=True, null=True)
    inf_tosse = models.IntegerField(blank=True, null=True)
    inf_coriza = models.IntegerField(blank=True, null=True)
    inf_outros = models.IntegerField(blank=True, null=True)
    inf_rbv_codigo = models.IntegerField(blank=True, null=True)
    inf_rcc_codigo = models.ForeignKey('InformacaoTbracacor', models.DO_NOTHING)
    inf_sex_codigo = models.ForeignKey('InformacaoTbsexos', models.DO_NOTHING)
    inf_idapi = models.CharField(max_length=50)
    def __str__ (self):
         return self.inf_idapi

    class Meta:
        managed = False
        db_table = 'informacao_tbinformacoes'
