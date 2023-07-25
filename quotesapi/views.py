from django.shortcuts import render
import json
import requests
import random

def home(request):
    import json
    import requests
    import random    

    api_request = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes/")

    try:
        api = json.loads(api_request.content)
        random_item = random.choice(api)
    except Exception as e:
        api = "Error..."    
    
    return render(request, 'home.html', {'random_item': random_item})

def about(request):
    return render(request, 'about.html', {})   

def wife(request):
    import json
    import requests
    import random   
    
    api_request = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes/search/wife")

    try:
        api = json.loads(api_request.content)
        wife_item = random.choice(api)
    except Exception as e:
        api = "Error..."    
    
    return render(request, 'wife.html', {'wife_item': wife_item})     

def work(request):
    import json
    import requests
    import random   
    
    api_request = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes/search/work")

    try:
        api = json.loads(api_request.content)
        work_item = random.choice(api)
    except Exception as e:
        api = "Error..."    
    
    return render(request, 'work.html', {'work_item': work_item})     

def food(request):
    import json
    import requests
    import random   
    
    api_request = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes/search/food")

    try:
        api = json.loads(api_request.content)
        food_item = random.choice(api)
    except Exception as e:
        api = "Error..."    
    
    return render(request, 'food.html', {'food_item': food_item})  

def random(request):  
    import json
    import requests
    import random     

    api_request = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes/")

    try:
        api = json.loads(api_request.content)
        random_item = random.choice(api)
    except Exception as e:
        api = "Error..."    
    
    return render(request, 'random.html', {'random_item': random_item})      


