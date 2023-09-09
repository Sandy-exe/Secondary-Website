from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.http import JsonResponse
import openai
  
openai.api_key = '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'
  
def get_completion(prompt):
    print("ok")
    print(prompt)
    query = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    model_lst = openai.Model.list()
    for i in model_lst['data']:
        print(i['id'])
    response = query.choices[0].text
    print(response)
    return response
  
  
def query_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        print("Response: ",response)
        return JsonResponse({'response': response})
    return render(request, 'index.html')
