import requests
import sys,os

try:
    #file = open('PHP.fuzz.txt', "r")
    file = open('file', "r")
    lines = file.readlines()
    file.close()

    for line in lines:
#        print(line.strip())
        url = "http://challenge01.root-me.org/web-serveur/ch11/"+line.strip()
        response = requests.get(url)
        print ("/tURL = ",url)
        if  not '404' in str(response):
            print(response)
            print(response.text)
#    response_json = response.json()
#    print(response_json)

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #fname => name of file
    print("Erreur  =====>  ",e," : ",exc_type," Line ", exc_tb.tb_lineno)
    print(e)

