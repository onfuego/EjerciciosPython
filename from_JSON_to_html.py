import requests
import json

#Solicitar el URL y el api key 
def request(url, api_key):

	url_final = url + api_key
#Se genera la solicitud al API 
	payload = ""
	headers = {
	    'User-Agent': "PostmanRuntime/7.11.0",
	    'Accept': "*/*",
	    'Cache-Control': "no-cache",
	    'Postman-Token': "47689ef7-439a-41b6-b540-5c49a63a2137,21eaa7a9-e512-41c0-ba5b-0e1976fd78f5",
	    'Host': "api.nasa.gov",
	    'accept-encoding': "gzip, deflate",
	    'Connection': "keep-alive",
	    'cache-control': "no-cache"
	    }

	response = requests.request("GET", url_final, data=payload, headers=headers)
#Nos devuelve el JSON 
	return json.loads(response.text)

#Funcion que construye el .html con el JSON obtenido
def build_web_page(data):
#Se genera el html vacio para concatenar formato .html con fotografias obtenidas del JSON
	html_vacio = ""
#Formato HTML
	html = "<html>\n<head>\n</head>\n<body>\n<ul>"

	photos = data["photos"][0:10]
#Se itera para buscar cada foto en la variable "photos"
	for index, elementos in enumerate(photos):
		html += "\t<li><img src=\"{}\"></li>\n".format(photos[index]["img_src"])
#Formato HTML
	html += "</ul>\n</body>\n</html>"
#Se genera el output del archivo .html que se guarda en la misma ubicacion que este archivo 
	with open("output.html", "w") as f:
		f.write(html)



