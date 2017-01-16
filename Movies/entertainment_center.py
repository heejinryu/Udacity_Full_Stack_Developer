# -*- coding: utf-8 -*-
import fresh_tomatoes
import media

# Creating Movie List

# Link of Charles theater to shorten the image URLs.
thecharles_link = "https://thecharles.com/wp-content/uploads/"

# La La Land: Story, Poster image and Movie trailer
# Each instance variables are defined first
# and the instance of Movie class created.
la_la_land_story = "In Los Angeles, aspiring actress Mia (Emma Stone) \
    serves lattes to movie stars in between auditions \
    while dedicated jazz musician Sebastian (Ryan Gosling) plays \
    in dingy bars in order to scrape by. The two meet and fall in love, \
    but, as success mounts, the dreams they worked so hard to maintain \
    threaten to tear them apart."
la_la_land_img = thecharles_link + "2016/11/La-La-Land-poster-876x1298.jpg"
la_la_land_trailer = "https://www.youtube.com/watch?v=0pdqf4P9MB8"
la_la_land = media.Movie(
    "La La Land",
    la_la_land_story,
    la_la_land_img,
    la_la_land_trailer)

# Barry Lyndon: Story, Poster image and Movie trailer
# Each instance variables are defined first
# and the instance of Movie class created.
barry_lyndon_story = "This personal, idiosyncratic, melancholy, \
    and long (three hours) adaptation of the Thackeray novel \
    is exquisitely shot in natural light (or, in night scenes, candlelight) \
    by John Alcott, with frequent use of slow backward zooms \
    that distance us, both historically and emotionally, \
    from its rambling picaresque narrative about \
    an 18th-century Irish upstart (Ryan O’Neal)…"
barry_lyndon_img = thecharles_link + "2016/12/barry-lyndon-poster-old.jpg"
barry_lyndon_trailer = "https://www.youtube.com/watch?v=9lzSoKOs1fc"
barry_lyndon = media.Movie(
    "Barry Lyndon",
    barry_lyndon_story,
    barry_lyndon_img,
    barry_lyndon_trailer)

# The Third Man: Story, Poster image and Movie trailer
# Each instance variables are defined first
# and the instance of Movie class created.
the_third_man_story = "The most famous collaboration of \
    the director Carol Reed and the screenwriter Graham Greene \
    has the structure of a good suspense thriller \
    and an atmosphere of baroque, macabre decadence.\
    The simple American, Joseph Cotten, arrives in postwar Vienna \
    to meet an old friend, only to be told that the friend has been \
    killed in an accident..."
the_third_man_img = thecharles_link + \
    "2016/12/219b3cc0e74bf1ad073d9e3dab1a571c.jpeg"
the_third_man_trailer = "https://www.youtube.com/watch?v=F-QWLAndD1E"
the_third_man = media.Movie(
    "The Third Man",
    the_third_man_story,
    the_third_man_img,
    the_third_man_trailer)

# Creating webpage using Fresh Tomatoes
movies = [la_la_land, barry_lyndon, the_third_man]
fresh_tomatoes.open_movies_page(movies)
