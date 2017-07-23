""" utlizes fresh_tomatoes to serve a webpage of movies """

import media
from fresh_tomatoes import open_movies_page


# Setup a list of my favorite movies.
movies = []
movies.append(media.Movie("The Princess Bride",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMGM4M2Q5N2MtNThkZS00NTc1LTk1NTItNWEyZjJjNDRmNDk5XkEyXkFqcGdeQXVyMjA0MDQ0Mjc@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=VYgcrny2hRs"))
movies.append(media.Movie("Meet the Robinsons",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg0NTU4MDY5OV5BMl5BanBnXkFtZTcwMzY0MjM0MQ@@._V1_.jpg",
                          "https://www.youtube.com/watch?v=S396-fnLldk"))
movies.append(media.Movie("Inside Out",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=yRUAzGQ3nSY"))

# Use the fresh_tomatoes module to create and open the webpage.
open_movies_page(movies)
