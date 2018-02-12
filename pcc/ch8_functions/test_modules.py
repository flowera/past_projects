import functions_note as fn
list_al = []
list_al.append(fn.make_album("Avril Lavigne", "Live in Calgary"))
list_al.append(fn.make_album("Taylor Swift", "1989"))
list_al.append(fn.make_album("Avril Lavigne", "Let Go", 13))
print (list_al)

while True:
    print("Please tell me the artist name:")
    print('Enter "q" at any time to quit!')
    art_n = input("Artist Name: ")
    if art_n == "q":
        break
    album_n = input("Album Name: ")
    if album_n == 'q':
        break
    no_t = input("Number of Tracks: ")
    if no_t == 'q':
        break
    album = fn.make_album(art_n, album_n, no_t)
    print(album)
#8-15 Printing Models
