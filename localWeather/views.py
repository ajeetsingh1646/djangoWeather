from django.shortcuts import render

def index(request):
    import json
    import requests
    
    api_request = requests.get("https://api.waqi.info/feed/here/?token=f6320186d06d4bc2ed866ab0fe51bfd6163b72f4")
    if request.method == "POST":
        city1 = request.POST['city1']
        api_request = requests.get("https://api.waqi.info/feed/"+city1+"/?token=f6320186d06d4bc2ed866ab0fe51bfd6163b72f4")
        try:
            api = json.loads(api_request.content)
            #a = api.data.aqi
            #status = ""
        except Exception as e:
            api = "Error..."
        
        aq = api["data"]["aqi"]
        if aq > 0 and aq < 50:
            category_color = "good"
                
        if aq > 50 and aq < 100:
            category_color = "moderate"
            
        if aq > 100 and aq < 150:
            category_color = "usg"
                
        if aq > 150 and aq < 200:
            category_color = "unhealthy"
                
        if aq > 200 and aq < 300:
            category_color = "veryunhealthy"
            
        if aq > 300:
            category_color = "hazardous"
            
        
        return render(request,'index.html',{"api" : api,"aq" : api["data"]["aqi"],"category_color" : category_color})
    
    
    try:
        api = json.loads(api_request.content)
        #a = api.data.aqi
        #status = ""
    except Exception as e:
        api = "Error..."
    
    aq = api["data"]["aqi"]
    if aq > 0 and aq < 50:
        category_color = "good"
            
    if aq > 50 and aq < 100:
        category_color = "moderate"
        
    if aq > 100 and aq < 150:
        category_color = "usg"
            
    if aq > 150 and aq < 200:
        category_color = "unhealthy"
            
    if aq > 200 and aq < 300:
        category_color = "veryunhealthy"
        
    if aq > 300:
        category_color = "hazardous"
        
    
    return render(request,'index.html',{"api" : api,"aq" : api["data"]["aqi"],"category_color" : category_color
                                       })
        


def about(request):
    return render(request, 'about.html',{})


