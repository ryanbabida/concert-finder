import tkinter
from PIL import ImageTk, Image
import json
import requests

root = tkinter.Tk()
root.title("ConcertFinder Beta")
root.geometry("800x250")

searchArtistFrame = tkinter.Frame(root)
searchArtistFrame.pack(side = tkinter.TOP)
labelArtist = tkinter.Label(searchArtistFrame, width = 17, height = 1, text = "Enter an Artist: ")
labelArtist.pack(side = tkinter.LEFT)
entryArtist = tkinter.Entry(searchArtistFrame, width=30)
entryArtist.pack(side = tkinter.LEFT)
searchArtistButton = tkinter.Button(searchArtistFrame, width = 2, height = 1, text = "Go")
searchArtistButton.pack(side = tkinter.LEFT)

listConcerts = tkinter.Listbox(root, width = 100)
listConcerts.pack(side = tkinter.TOP)

def searchArtistBut():
	searchArtist(entryArtist.get())

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

searchArtistButton.configure(command = searchArtistBut)

root.mainloop()