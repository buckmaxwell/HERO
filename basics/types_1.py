# bool (Boolean) values are True or False
call_me = (
    True  # https://open.spotify.com/track/3TGRqZ0a2l1LRblBkJoaDx?si=df0367a7dc1d481f
)
print(type(call_me))

# int (Integer) values
number_of_little_birds = (
    3  # https://open.spotify.com/track/7vggqxNKwd6xdRoYS0pQtM?si=b10e255c52a7465d
)
print(type(number_of_little_birds))

# float (Decimal numbers)
seconds_from_wilding = 4.5
print(
    type(seconds_from_wilding)
)  # https://open.spotify.com/track/78TTtXnFQPzwqlbtbwqN0y?si=8ebf8094b34b4461

# str (String) values are a collection of characters. Characters don't get a special type in python.
BIRDS_OF_A_FEATHER = (
    "https://open.spotify.com/track/6dOtVTDdiauQNBQEDOtlAB?si=1b3237b2d824466e"
)
print(
    type(BIRDS_OF_A_FEATHER)
)  # ALL CAPS is usually used to refer to variables who's values won't change or constants

# list
lou_begas_girlfriends = [
    "Angela",
    "Pamela",
    "Sandra",
    "Rita",
    "Monica",
    "Erica",
    "Tina",
    "Sandra",
    "Mary",
    "Jessica",
]
print(
    type(lou_begas_girlfriends)
)  # https://open.spotify.com/track/6x4tKaOzfNJpEJHySoiJcs?si=5849846939664f6c


favorite_artist = {
    "Angela": "The Proclaimers",
    "Pamela": "Whitney Houston",
    "Sandra": "Bruno Mars",
    "Rita": "Miley Cyrus",
    "Monica": "Carly Rae Jepsen",
    "Erica": "LCD Soundsystem",
    "Tina": "Salt-N-Pepa",
    "Sandra": "Pharrell Williams",
    "Mary": "Taylor Swift",
    "Jessica": "Katy Perry",
}
print(favorite_artist)
