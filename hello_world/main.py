from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

from django import forms
from django.shortcuts import render
from django.http import HttpResponse

def submit(request):
    if request.method == 'POST':
        text = request.POST.get('text')  # Get the input with name "text"
        reply = model.generate("Symptoms are: " + text + "What is the diagnosis? ", max_tokens=3)
        return HttpResponse(reply)
    return render(request, 'templates/index.html')


