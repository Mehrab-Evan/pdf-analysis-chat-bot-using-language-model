
# Both are same code
# from transformers import pipeline
#
# classifier = pipeline("sentiment-analysis")
#
# res = classifier("I've been waiting for a huggingface course whole life")
#
# print(res)
# Both are same code 2-9 and 13 - 27


# Both are same code
# ----------------------------------
from transformers import pipeline

# Specify the model name and revision
model = "distilbert-base-uncased-finetuned-sst-2-english"
revision = "af0f99b"

# Create the sentiment analysis pipeline with the specified model
classifier = pipeline("sentiment-analysis", model=model, revision=revision)

# Perform sentiment analysis on a sample text
res = classifier("I need to marry but I don't have money")

print(res)

# -------------------------------------------









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