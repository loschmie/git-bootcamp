imelda = 'More Mayhem', 'Imelda May', 2011, [(1, 'Pulling the Rung'), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")]
album, artist, year, tracks = imelda
print('Album: {}\nArtist: {}\nYear: {}'.format(album, artist, year))
print('Track List:')
for song in tracks:
    track, title = song
    print('\ttrack number:{} song title:{}'.format(track, title))
    
      
