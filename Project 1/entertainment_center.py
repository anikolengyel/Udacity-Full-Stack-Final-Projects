import media
import fresh_tomatoes


# create instances of movies based on the constructor in media.py
# the instances have the following variables: title, poster image, trailer

toy_story = media.Movie(
    "Toy Story",
    "https://upload.wikimedia.org/wikipedia/commons/8/8a/"
    "Toy_Stoy_3_logo.svg",
    "https://www.youtube.com/watch?v=Ny_hRfvsmU8")

back_to_the_future = media.Movie(
    "Back to the Future",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/"
    "Back_to_the_Future.jpg",
    "https://www.youtube.com/watch?v=MdENmefJRpw")

avatar = media.Movie(
    "Avatar",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=6ziBFh3V1aM")

spirit = media.Movie(
    "Forest Gump",
    "https://upload.wikimedia.org/wikipedia/en/6/67/"
    "Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=bLvqoHBptjg")

slumdog_millionaire = media.Movie(
    "Slumdog Millionaire",
    "https://upload.wikimedia.org/wikipedia/en/9/92/"
    "Slumdog_Millionaire_poster.png",
    "https://www.youtube.com/watch?v=AIzbwV7on6Q")

life_is_beautiful = media.Movie(
    "Life is Beautiful",
    "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",
    "https://www.youtube.com/watch?v=8CTjcVr9Iao")

movies = [toy_story, back_to_the_future, avatar, spirit, slumdog_millionaire,
          life_is_beautiful]
fresh_tomatoes.open_movies_page(movies)
