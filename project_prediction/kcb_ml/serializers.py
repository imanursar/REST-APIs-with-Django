from rest_framework import serializers
from kcb_ml.models import Kcb


class KcbSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kcb
        fields = ('ext_source_2',
                  'ext_source_3',
                  'good_price_to_credit_ratio',
                  'days_birth',
                  "amt_goods_price",
                  "avg_days_credit_update",
                  "avg_days_first_drawing",
                  "days_employed",
                  "count_refused_prev",
                  "count_hc_reject_prev",
                  "max_rate_down_payment",
                  "count_short_term",
                  "avg_amt_annuity_prev",
                  "days_id_publish",
                  "avg_days_enddate_fact",
                  "count_prev_pos",
                  "days_last_phone_change",
                  "prob_topay"
                  )
