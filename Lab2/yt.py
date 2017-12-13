#Part 1
from urllib.request import *
from bs4 import *
import pyexcel
from youtube_dl import YoutubeDL
webpage = urlopen('https://www.apple.com/itunes/charts/songs/')
data = webpage.read()
html_content = data.decode('utf-8')

soup = BeautifulSoup(html_content,'html.parser')
section = soup.find('section',{'class':'section chart-grid'})
div = section.find('div',{'class':"section-content"})
ul = div.find('ul')
li_list = ul.find_all('li')
list_upload = []
for li in li_list:
    stt = li.strong
    name = li.h3.a
    artist = li.h4.a
    songs = {
        'STT': stt.string,
        'Song': name.string,
        'Artist': artist.string
    }
    list_upload.append(songs)
pyexcel.save_as(records=list_upload, dest_file_name="Topchart.xlsx")
#Part 2
options = {
    'default_search': 'ytsearch',
    'max_downloads': len(list_upload)
}
dl = YoutubeDL(options)
for musicdown in list_upload:
    dl.download([musicdown['Artist'] +" "+ musicdown['Song']])
