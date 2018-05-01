import webbrowser


class Movie():
    """Documentation for the movies website to test
    Python's __doc__ class variable."""

    # create the class properties for the Movie class
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # a function to open the webpage for every movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
