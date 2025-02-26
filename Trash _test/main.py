from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

print(r'''
  ____           _ _          ____ ____ _____ 
 |  _ \ __ _  __| (_)_ __    / ___|  _ \_   _|
 | |_) / _` |/ _` | | '_ \  | |  _| |_) || |  
 |  _ < (_| | (_| | | | | | | |_| |  __/ | |  
 |_| \_\__,_|\__,_|_|_| |_|  \____|_|    |_|  ''' )
print('Generating answer... \n')

while True:
  prompt = input('Prompt --> ')
  print('')

  completion = client.chat.completions.create(
    extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="deepseek/deepseek-r1:free",
  messages=[
    {
      "role": "user",
      "content": f"${prompt}"
    }
  ]
  )
  print(completion.choices[0].message.content)
  print('')