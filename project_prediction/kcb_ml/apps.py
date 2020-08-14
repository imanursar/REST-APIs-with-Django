from django.apps import AppConfig
import pickle
import datetime
import dill
import numpy as np

import warnings
warnings.filterwarnings("ignore")

class kcb_mlConfig(AppConfig):
    name = 'kcb_ml'


class PredictorConfig(AppConfig):

    def get_ai_grade(prob):
        d = dict()
        if prob <= 50:
            grade = 'bad'
            description = 'ditolak'
        else:
            grade = 'good'
            description = 'diterima'
        d['grade'] = grade
        d['description'] = description
        return d

    def predict(data,headers):
        time_1 = datetime.datetime.now()
        model_AI = pickle.load(open(f"data/KS_41_pickle.pkl",'rb'))
        lime_AI = dill.temp.loadIO(pickle.load(open(f'data/KS_41_lime.pkl','rb')))

        data_temp = [[
                    data.get('ext_source_2'),
                    data.get('ext_source_3'),
                    data.get('good_price_to_credit_ratio'),
                    data.get('days_birth'),
                    data.get('amt_goods_price'),
                    data.get('avg_days_credit_update'),
                    data.get('avg_days_first_drawing'),
                    data.get('days_employed'),
                    data.get('count_refused_prev'),
                    data.get('count_hc_reject_prev'),
                    data.get('max_rate_down_payment'),
                    data.get('count_short_term'),
                    data.get('avg_amt_annuity_prev'),
                    data.get('days_id_publish'),
                    data.get('avg_days_enddate_fact'),
                    data.get('count_prev_pos'),
                    data.get('days_last_phone_change')]]


        prob_topay = model_AI.predict_proba(data_temp)[0][1]
        grade = PredictorConfig.get_ai_grade(prob_topay*100)

        out_dict = dict()
        out_dict['prob_topay'] = round((float(prob_topay))*100, 3)
        out_dict['grade'] = grade

        if(headers == 'y'):
            time1 = datetime.datetime.now()
            data_temp_ar = np.array(data_temp)
            exp = lime_AI.explain_instance(data_temp_ar[0], model_AI.predict_proba, num_features=20)
            # print(exp.as_list())
            data_columns = ["ext_source_2","ext_source_3","good_price_to_credit_ratio","days_birth","amt_goods_price","avg_days_credit_update","avg_days_first_drawing","days_employed","count_refused_prev","count_hc_reject_prev","max_rate_down_payment","count_short_term","avg_amt_annuity_prev","days_id_publish","avg_days_enddate_fact","count_prev_pos","days_last_phone_change"] # urutannya harus sesuai dengan columns pd lime
            criterias = []
            values = []
            for column in data_columns:
                for criteria in [item[0] for item in exp.as_list()]:
                    if (column in criteria):
                        col = column
                        values.append(exp.as_list()[[item[0] for item in exp.as_list()].index(criteria)][1])
                        criterias.append(col)
            values = [ round(elem, 4) for elem in values ]
            out_dict['criterias'] = criterias
            out_dict['values'] = values
            time2 = datetime.datetime.now()
            timedel_1 = time2 - time1
            out_dict['time_span_2'] = round((timedel_1.total_seconds()), 4)
            # out_dict = dict(zip(criterias,values))

        time_2 = datetime.datetime.now()
        timedel = time_2 - time_1
        out_dict['time_span_1'] = round((timedel.total_seconds()), 4)
        return(out_dict)
