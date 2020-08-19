from django.contrib import admin
from .models import Kcb

# Register your models here.


class KcbAdmin(admin.ModelAdmin):
    #Fields
    fields =("id",("ext_source_2","ext_source_3"),"good_price_to_credit_ratio","days_birth","amt_goods_price","avg_days_credit_update","avg_days_first_drawing","days_employed","count_refused_prev","count_hc_reject_prev","max_rate_down_payment","count_short_term","avg_amt_annuity_prev","days_id_publish","avg_days_enddate_fact","count_prev_pos","days_last_phone_change")

    #List Display
    list_display = ("id","ext_source_2",'amt_goods_price','days_id_publish')

    #List_filter
    list_filter = ("good_price_to_credit_ratio",'amt_goods_price')

    #ordering
    # ordering = ('<model_field_names>')

    #fieldsets
    # fieldsets =(
    #             ('Required information',{
    #                 'description' : '<'description_sentence>',
    #                 'fields':('<model_fields'>)
    #             }),
    #             ('Optional Information',{
    #                 'classes' : ('collapse',),
    #                 'fields': ('<model_fields>')
    #             })
    #     )

admin.site.register(Kcb,KcbAdmin)
