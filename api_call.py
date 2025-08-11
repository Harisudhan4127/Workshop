import openai

openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

user_input = input("You : ")
reply = ""

response = openai.ChatCompletion.create(
    model = "mistralai/mistral-7b-instruct",
    messages = [{"role" : "System", "content": "you are helpful"},
                {"role": "user", "content" : user_input},
                {"role": "assistant", "content": reply}])
reply = response['choices'][0]['message']['content']
print(f"Chat-Bot : {reply}\n")
