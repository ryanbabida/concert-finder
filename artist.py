import json
import requests
import gui

def searchArtist(name):
	name = name.replace(" ","%20")
	name = name.replace("/","%252F")
	name = name.replace("?","%252F")

	response = requests.get('http://api.bandsintown.com/artists/%s/events.json?api_version=2.0&app_id=YOUR_APP_ID' % name)
	artist_data = json.loads(response.text)

	concertCount = 0;

	listConcerts.delete(0, listConcerts.size())
	for i in artist_data:
	    listConcerts.insert(concertCount, i['title'] + " " + i['formatted_datetime'])
	    concertCount = concertCount + 1