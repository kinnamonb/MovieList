""" Contains the various types of media. """


class Movie():
    """ A movie

    title -- The title of the movie.
    cover -- The URL of the movie's cover image.
    trailer -- The URL of the movie's trailer.
    """

    def __init__(self, title, cover, trailer):
        """ Initializes the Movie's properties """
        self.title = title
        self.cover = cover
        self.trailer = trailer
