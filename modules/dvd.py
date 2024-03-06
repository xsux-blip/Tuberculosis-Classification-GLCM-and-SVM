# modules/dvd.py

class Dvd:
    def __init__(self, title, subject, upc, genre, actors=None, directors=None):
        self.title = title
        self.subject = subject
        self.upc = upc
        self.genre = genre
        self.actors = actors
        self.directors = directors
