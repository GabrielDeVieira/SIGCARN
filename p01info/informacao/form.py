from django.forms import ModelForm
from atividade.models import TbInformacoes, TbRacacor


class TbRacacorForm(ModelForm):
    class Meta:
        model = TbRacacor
        fields = ["rcc_racacor", "rcc_codigo"]
class TbInformacoesForm(ModelForm):
    class Meta:
        model = TbInformacoes
        fields = ["inf_idade", "inf_idsus", "inf_datainiciosintomas", "inf_datadeinsercao", "inf_assintomatico",
        "inf_dordecabeca", "inf_febre", "inf_disturbios", "inf_gustativos", "inf_dordegarganta", "inf_disturbiosolfativos",
         "inf_dispneia", "inf_tosse", "inf_coriza", "inf_outros", "inf_rcc_codigo", "inf_sex_codigo", "inf_rbv_codigo",
         ]

