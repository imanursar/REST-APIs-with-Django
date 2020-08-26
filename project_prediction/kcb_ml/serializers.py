from rest_framework import serializers
from kcb_ml.models import Kcb,Kcb_result
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class KcbSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kcb
        fields = ('userID',
                  'ext_source_2',
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
                  "days_last_phone_change"
                  )

class KcbSerializer_result(serializers.ModelSerializer):

    class Meta:
        model = Kcb_result
        fields = ('userID',
                  "prob_topay",
                  )
