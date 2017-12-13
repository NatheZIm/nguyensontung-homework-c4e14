from youtube_dl import YoutubeDL
#Download a single youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=EtFBjd4k1Ow'])


# Download multiple youtube videos
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=4-xOsc3NZvA', 'https://www.youtube.com/watch?v=Sup6oHC4yrE'])

#Download audio
options = {
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=JZjRrg2rpic'])



#Search and then download the first video
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])


#Search and then download the first audio
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Nhớ mưa sài gòn lam trường'])
