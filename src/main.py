import openai
import os

def ask_gpt(text):
  openai.api_key = os.getenv("openai_api_key")
  response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = text,
    temperature = 0.6,
    max_tokens = 150,
  )
  return print(response.choices[0].text)
  
def main():
  while True:
    print('GPT: Ask me a question\n')
    myQn = input()
    ask_gpt(myQn)
    print('\n')

main()