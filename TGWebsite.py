def web(str):
    import urllib.request
    import webbrowser
    #str="Dagdu Sheth Pune"
    get_url=webbrowser.open(f'https://www.google.com/search?q={str}')

    get_url=urllib.request.urlopen(f'https://www.google.com/search?q={str}')

    print("Response Status: "+str(get_url.getcode()))
    print(get_url.write())
