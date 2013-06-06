"""
find_lyrics, a simple text based lyrics retrieval application.
Srinidhi Kaushik, shrinidhi.kaushik@gmail.com, 06/06/13.
"""
#!/usr/bin/python
import re
import html2text
import urllib2
from BeautifulSoup import BeautifulSoup

def find_lyrics(song, band):
	song_copy = song
	band_copy = band
	song = re.sub('[^A-Za-z0-9]', '+', song.lower())
	band = re.sub('[^A-Za-z0-9]', '+', band.lower())
	song = re.sub('\+\+', '', song)
	band = re.sub('\+\+', '', band)
	match_expr = band + "\/" + song
	flag = 0
	possible = []
	
	html_page = urllib2.urlopen("http://search.azlyrics.com/search.php?q="+str(song))
	soup = BeautifulSoup(html_page)
	
	for link in soup.findAll('a', attrs={'href': re.compile(match_expr)}):
		possible.append(link.get('href'))
 	
 	if (len(possible) == 0):
 		print("\nCouldn\'t retrieve lyrics.")
 		exit()
 	
 	print("\n" + song_copy + ", by " + band_copy + ":")
	
	new_html = urllib2.urlopen(possible[0]).readlines()
	for line in new_html:
		if (re.match("<!-- start of lyrics -->", line)):
			flag = 1
		elif (re.match("<!-- end of lyrics -->", line)):
			flag = 0
		if (flag == 1):
			line = re.sub('<[^<]+?>', '', line)
			if (line != "\n" or line != ""):
				line = re.sub("\n", '', line)
				print(line)

def main():
	print("find_lyrics")
	song = raw_input("Song: ")
	band = raw_input("Artist/Band name: ")
	find_lyrics(str(song), str(band))
	print("")

if __name__ == '__main__':
	main()