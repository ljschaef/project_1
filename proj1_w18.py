import requests
import json


class Media:

    def __init__(self, title="No Title", author="No Author", year="No Year", url= "no url", json_dict=None):
        if json_dict is not None:
            self.title = json_dict["collectionName"]
            self.author = json_dict["artistName"]
            self.year = json_dict["releaseDate"]
            self.release_year = self.year[0:4]
            self.url = json_dict[""]
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
                 length= 0, url= "no url", json_dict=None):
        if json_dict is not None:
            self.title = json_dict["trackName"]
            self.author = json_dict["artistName"]
            self.year= json_dict["releaseDate"]
            self.release_year = self.year[0:4]
            self.album = json_dict["collectionName"]
            self.genre = json_dict["primaryGenreName"]
            self.length = json_dict["trackTimeMillis"]
        else:
            super().__init__(title, author, year)
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
                 movie_length=0, url= "no url", json_dict=None):
        if json_dict is not None:
            self.title = json_dict["trackName"]
            self.author = json_dict["artistName"]
            self.year = json_dict["releaseDate"]
            self.release_year = self.year[0:4]
            self.rating = json_dict["contentAdvisoryRating"]
            try:
                self.movie_length = json_dict["trackTimeMillis"]
            except:
                self.movie_length = "None"
        else:
            super().__init__(title, author, year)
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
    json_file.close()
    return json.loads(json_stuff)

if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
    user = input("Enter a search term or enter exit to quit")
    while user != "exit":
        base_url = 'https://itunes.apple.com/search?'
        t = ""
        json_string = requests.get(base_url, params={'term': t})
        results_list = json.loads(json_string.text)['results']
        counter = 1
        for a in results_list:
            if a["wrapperType"] == "track":
                if a["kind"] == "song":
                    s1 = proj1.Song(json_dict=a)
                    print(counter + ". " + s1)
                    counter += 1
                else:
                    mo1 = proj1.Movie(json_dict=a)
                    print(counter + ". " + mo1)
                    counter += 1
            else:
                m1 = proj1.Media(json_dict=a)
                print(counter + ". " + m1)
                counter += 1
        mehr_input = input("Enter a search term, enter number of term to launch preview, or enter exit to quit")
        if mehr_input.isdigit():
            search = results_list[int(mehr_input)]
            if search.url != "no url":
                webbrowswer.open(search.url)
        elif mehr_input != "exit":

    exit()
