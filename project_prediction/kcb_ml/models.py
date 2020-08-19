# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Kcb(models.Model):
    userID = models.IntegerField()
    ext_source_2 = models.FloatField()
    ext_source_3 = models.FloatField()
    good_price_to_credit_ratio = models.FloatField()
    days_birth = models.IntegerField()
    amt_goods_price = models.IntegerField()
    avg_days_credit_update = models.FloatField()
    avg_days_first_drawing = models.FloatField()
    days_employed = models.IntegerField()
    count_refused_prev = models.IntegerField()
    count_hc_reject_prev = models.IntegerField()
    max_rate_down_payment = models.FloatField()
    count_short_term = models.IntegerField()
    avg_amt_annuity_prev = models.FloatField()
    days_id_publish = models.IntegerField()
    avg_days_enddate_fact = models.FloatField()
    count_prev_pos = models.IntegerField()
    days_last_phone_change = models.IntegerField()


    class Meta:
        db_table = 'kcb'
        #ordering = ['days_birth']

    def __str__(self):
        return f"{self.days_birth} : {self.days_employed}"

class Kcb_result(models.Model):
    # data = models.ForeignKey(Kcb, on_delete=models.CASCADE)
    userID = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    prob_topay = models.FloatField()


    class Meta:
        db_table = 'kcb_result'
        #ordering = ['days_birth']

    def __str__(self):
        return f"{self.id} : {self.prob_topay}"
