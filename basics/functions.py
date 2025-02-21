# funtions are like machines that take in input and give out output
def add(a, b):
    return a + b


print(add(1, 2))

NUMBER_OF_MILES = 500

print(
    f"""I would walk {NUMBER_OF_MILES} miles, and I would walk {NUMBER_OF_MILES} more. """
    f"""Just to be the man who walked {add(NUMBER_OF_MILES, NUMBER_OF_MILES)} miles to fall down at your door."""
)


# but they can do more interesting things than just adding numbers
def get_lou_begas_girlfriends_favorite_artist(girlfriend):
    FAVORITE_ARTIST = {
        "Angela": "The Proclaimers",
        "Erica": "Fleetwood Mac",
        "Jessica": "Katy Perry",
        "Mary": "Taylor Swift",
        "Monica": "Carly Rae Jepsen",
        "Pamela": "Whitney Houston",
        "Rita": "Miley Cyrus",
        "Sandra": "Bruno Mars",
        "Tina": "Salt-N-Pepa",
    }
    return FAVORITE_ARTIST[girlfriend]


print(get_lou_begas_girlfriends_favorite_artist("Angela"))
