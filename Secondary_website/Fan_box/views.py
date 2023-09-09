from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.http import JsonResponse
import openai
  
openai.api_key = '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'

global save_context

save_context =[
        {"role": "system", "content": "You are Fanbox, who helps to clear doubts related to fiction. "},
        {"role": "user", "content": "Who are you?"},
        {"role": "assistant", "content": "I'm a fanbox, who helps fans to clear your doubts related to fiction "}]

def get_completion(prompt):
    global save_context
    save_context.append({"role": "user", "content": prompt})
    query = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
        messages=save_context,
    )
    
    # model_lst = openai.Model.list()
    # for i in model_lst['data']:
    #     print(i['id'])
    response = query['choices'][0]['message']['content']
    save_context.append({"role": "assistant", "content": response})
    print("\n\n")
    for i in save_context:
        print(i["role"],":",i["content"])
    print("\n\n")
    return response

  
  
def query_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        return JsonResponse({'response': response})
    return render(request, 'index.html')
