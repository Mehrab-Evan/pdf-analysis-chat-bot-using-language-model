import torch
from transformers import pipeline
import pandas as pd

tqa = pipeline(task="table-question-answering", model="google/tapas-base-finetuned-wtq")

my_table = pd.read_csv("data.csv")

my_table = my_table.astype(str)

my_query = "Which cities has 5 0 snowfall?"

print(tqa(table=my_table, query=my_query)['answer'])

# print(table)
