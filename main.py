from pytube import YouTube

print('Gib den Link vom Video ein!')
link = input('Link: ')

yt = YouTube(link)

print('Dieses Video wurde gefunden: ' + yt.title)
print('')
print(yt.streams)
print('')


stream_id_input = input('Gib die Stream id ein!  : ')
stream = yt.streams.get_by_itag(stream_id_input)
stream.download()