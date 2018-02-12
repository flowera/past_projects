def display_message():
    """Displays a message from me."""
    print("Chapter 8: Details about Functions, args are similar to parameters! Here we don't have args")
#display_message()
def fav_book(b_name):
    """Print your favourite book from input."""
    print("One of my favourite book is: " + b_name.title() + "!!!")
#fav_book("pthon crash course")
def make_shirt(text,size="large"):
    """Get text from input then print it on the size large shirt, large as default."""
    print("This shirt needs to be size: " + size + ", and print " +"'"+ text+"'" + " on it!")
#make_shirt("I love python!")
def city_country(city_n, country_n):
    """Print title case city and country."""
    res = city_n + ',' + ' ' + country_n
    return res.title()
#print(city_country("Beijing", "China"))

def make_album(artist_n, album_title, no_tracks = ''):
    """Make an album for given artist name, album title and number of tracks."""
    album = {"Artist Name": artist_n, "Album Title": album_title}
    if no_tracks:
        album["Number of Tracks"] = no_tracks
    return album
