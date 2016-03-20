import fresh_tomatoes


class MovieObj():

    def __init__(self, title, poster_url, youtube_url):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url

# Create a list of My Movies and store them in a list
myMovies = []

myMovies.append(MovieObj(
    "Interstellar",
    "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX640_SY720_.jpg",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA"
))
myMovies.append(MovieObj(
    "Gravity",
    "http://ia.media-imdb.com/images/M/MV5BNjE5MzYwMzYxMF5BMl5BanBnXkFtZTcwOTk4MTk0OQ@@._V1_SX640_SY720_.jpg",
    "https://www.youtube.com/watch?v=OiTiKOy59o4"
))
myMovies.append(MovieObj(
    "The Martian",
    "http://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_SX640_SY720_.jpg",
    "https://www.youtube.com/watch?v=ej3ioOneTy8"
))

fresh_tomatoes.open_movies_page(myMovies)