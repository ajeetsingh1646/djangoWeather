from django.shortcuts import render

def index(request):
    import json
    import requests
    api_request = requests.get("https://api.waqi.info/feed/here/?token=f6320186d06d4bc2ed866ab0fe51bfd6163b72f4")
    try:
        api = json.loads(api_request.content)
        #a = api.data.aqi
        #status = ""
    except Exception as e:
        api = "Error..."
    
    return render(request,'index.html',{"api":api,
                                       "aq":api["data"]["aqi"]})


def about(request):
    return render(request, 'about.html',{})


