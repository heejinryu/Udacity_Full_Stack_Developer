import webbrowser

# Creating Movie class

class Movie():

# Initializing class variables
    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Show Trailer method opens a webbroswer with a trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
