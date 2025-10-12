#1
def city_country(city, country):
    full_address = f"{city}, {country}"
    return full_address.title()

address = city_country("cavity", "philippines")
print(address)
address = city_country("tokyo", "japan")
print(address)
address = city_country("paris", "france")
print(address)
address = city_country("toronto", "canada")
print(address)

#2
print("\n")
def make_album(artist_name, album_title, number_songs = None):
    album = {'artist': artist_name, 'album': album_title}
    if number_songs:
        album['number_songs': number_songs]
    
    return album

album = make_album(artist_name="Adele", album_title="Rolling in the Deep")
print(album)
album = make_album(artist_name="Ed Sheeran", album_title="Perfect")
print(album)
album = make_album(artist_name="Taylor Swift", album_title="Love Story")
print(album)

#3
print("\n")
while True:
    print("\nPlease enter album info:")
    artist = input("Enter artist name: ")
    title = input("Enter album title: ")

    album = make_album(artist_name=artist, album_title=title)
    print(album)
