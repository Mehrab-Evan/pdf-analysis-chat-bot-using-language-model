import openai
openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful AI Company recruiter. Your task is to ask company-related queries to job applicants. Your queries include topics related to the applicant's profile, his available hours, etc."},
        {"role": "user", "content": "I am Pradip, I want to apply to a job your company posted"},
        {"role": "assistant", "content": "Hello, Pradip. That's awesome! What do you want to know about AI?"},
        {"role": "user", "content": "What is the office hours?"}
    ]
)
response
