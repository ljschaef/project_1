import requests
import json


class Media:

    def __init__(self, title="No Title", author="No Author", year="No Year", json_dict=None):
        if json_dict is not None:
            if json_dict["wrapperType"] == "track":
                self.title = json_dict["trackName"]
            else:
                self.title = json_dict["collectionName"]
            self.author = json_dict["artistName"]
            self.year = json_dict["releaseDate"]
            self.year = self.year[0:3]
        else:
            self.title = title
            self.author = author
            self.release_year = year

    def __str__(self):
        return self.title + " by " + self.author + "(" + self.release_year + ")"

    def __len__(self):
        return 0

## Other classes, functions, etc. should go here
class Song(Media):
    def __init__(self, title= "No Title", author="No Author", year="No Year", album="No Album", genre="No Genre",
                 length= 0, json_dict=None):
        super().__init__(title, author, year, json_dict)
        if json_dict is not None:
            self.album = json_dict["collectionName"]
            self.genre = json_dict["primaryGenreName"]
            self.length = json_dict["trackTimeMillis"]
        else:
            self.album = album
            self.genre = genre
            self.length = length


    def __str__(self):
        return super().__str__() + "[" + self.genre + "]"

    def __len__(self):
        maybe = self.length
        seconds = maybe / 1000
        return seconds

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", year="No Release Year", rating="No Rating",
                 movie_length=0, json_dict=None):
        super().__init__(title, author, year, json_dict)
        if json_dict is not None:
            self.rating = json_dict["contentAdvisoryRating"]
            self.movie_length = json_dict["trackTimeMillis"]
        else:
            self.rating = rating
            self.movie_length = movie_length

    def __str__(self):
        return super().__str__() + "[" + self.rating + "]"

    def __len__(self):
        maybe = self.movie_length
        seconds = maybe / 1000
        minutes = seconds / 60
        remaining = seconds % 60
        if remaining >= 30:
            minutes += 1
        return minutes

def file_opener(json_dict):
    json_file = open(json_dict)
    json_file.read()
    pass

if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	pass
