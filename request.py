
def request(url, api_key):

	url_final = url + api_key

	print(url_final)

	import requests

	querystring = {"sol":"1000","api_key":str(api_key)}

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

	response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

	print(response.text)



def build_web_page(requested_url):
	import json
	import requests

	payload = ""
	headers = {
    	'cache-control': "no-cache",
    	'Postman-Token': "4037dcf6-fedb-4cf5-af10-e0d403894134"
    	}

	response = requests.request("GET", requested_url, data=payload, headers=headers)
	data = json.loads(response.text)

	html = ""

	photos = data["photos"]

	for photo in photos:
		html += "<img src=\"{}\">\n".format(photo["img_src"])


	with open("output.html", "w") as f:
		f.write(html)


