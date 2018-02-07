import requests
import json


class Media:

    def __init__(self, title="No Title", author="No Author", year="No Year", json_dict=None):
        if json_dict is not None:
            for a in json_dict:
                if a["wrapperType"] == "track":
                    if a["kind"] == "song":
                        Song(a)
                    else:
                        Movie(a)
                else:
                    self.title = a["collectionName"]
                    self.author = a["artistName"]
                    self.year = a["releaseDate"]
                    self.release_year = self.year[0:4]
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
        return int(seconds)

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
        return int(minutes)

def file_opener(filename):
    json_file = open(filename)
    json_stuff = json_file.read()
    return json.loads(json_stuff)

if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	pass
