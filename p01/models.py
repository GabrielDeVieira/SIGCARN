# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models





class InformacaoTbinformacoes(models.Model):
    inf_codigo = models.AutoField(primary_key=True)
    inf_idapi = models.CharField(unique=True, max_length=50)
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
    inf_evolucaocaso = models.IntegerField(db_column='inf_evolucaoCaso', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'informacao_tbinformacoes'


class InformacaoTbracacor(models.Model):
    rcc_codigo = models.IntegerField(primary_key=True)
    rcc_racacor = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informacao_tbracacor'


class InformacaoTbsexos(models.Model):
    sex_codigo = models.IntegerField(primary_key=True)
    sex_sexo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informacao_tbsexos'



