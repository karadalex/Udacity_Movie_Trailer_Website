import fresh_tomatoes


# Create a simple movie object to structure movie's info
class MovieObj():

    def __init__(self, title, poster_url, youtube_url):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url

# Create a list for My Movies
myMovies = []

# Open moviesDB.csv file where Movies Info is stored:
movies_database = open('moviesDB.csv', 'r').readlines()

# Iterate through the csv file, ignore 1st line;
for i in range(1, len(movies_database)):
    # Create a list out of each line containing [Movie Title, Movie Poster Image, Movie Youtube Trailer Video]
    movieInfo = movies_database[i].split(';')
    try:
        myMovies.append(MovieObj(
            movieInfo[0],
            movieInfo[1],
            movieInfo[2],
        ))
    except IndexError:
        break

fresh_tomatoes.open_movies_page(myMovies)