# -*- coding: utf-8 -*-

import os

from data_set import Dataset

from model_wrap import ModelSettings
from model_wrap import ModelClassification


os.environ['CUDA_VISIBLE_DEVICES'] = '0'

#
flag_load_data = True
model_tag = 'cnn'
#

#
pretrained_emb_file = None
emb_dim = 64
#
dataset = Dataset()
dataset.pretrained_emb_file = pretrained_emb_file
dataset.emb_dim = emb_dim
#
dataset.load_vocab_tokens_and_emb()
#

#
config = ModelSettings(dataset.vocab)
config.keep_prob = 1.0
config.model_tag = model_tag
#
model = ModelClassification(config)
model.prepare_for_prediction()
#


text_raw = ["这本书不错" ]

"""
work_book = xlrd.open_workbook(file_raw)
data_sheet = work_book.sheets()[0]
text_raw = data_sheet.col_values(0)
"""

#
preds_list = []
logits_list = []
#
for item in text_raw:
    logits = model.predict([ item ])
    pred = list(logits[0]).index(max(logits[0]))
    #
    logits_list.append(logits[0])
    preds_list.append(pred)
#
list_pair = zip(preds_list, text_raw)
#
for item in list_pair:
    print(item)


"""
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet')

for idx, item in enumerate(items_err):
    label = 'a' if item[1] == 1 else 'b'
    worksheet.write(idx, 0, ''.join(dataset.vocab.recover_from_ids(item[0]) ) )
    worksheet.write(idx, 2, label)

filepath = 'ab.xls'
if os.path.exists(filepath):
    os.remove(filepath)
workbook.save(filepath)

"""



