class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


if __name__ == "__main__":
    s1 = Song("99 Problems", "Jay-Z", "Rap")
    s2 = Song("Halo", "Beyonce", "Pop")
    s3 = Song("Empire State of Mind", "Jay-Z", "Rap")
    s4 = Song("Formation", "Beyonce", "Pop")

    print("Total Songs:", Song.count)
    print("Artists:", Song.artists)
    print("Genres:", Song.genres)
    print("Genre Count:", Song.genre_count)
    print("Artist Count:", Song.artist_count)

      

