
class Media:

    def __init__(self, title="No Title", author="No Author", year="No Year"):
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
                 length=0):
        super().__init__(title, author, year)
        self.album = album
        self.genre = genre
        self.length = length


    def __str__(self):
        return super().__str__() + "[" + self.genre + "]"

    def __len__(self):
        maybe = self.length
        
        return maybe

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", year="No Release Year", rating="No Rating",
                 movie_length="No Movie Length"):
        super().__init__(title, author, year)
        self.rating = rating
        self.movie_length = movie_length

    def __str__(self):
        return  super().__str__() + "[" + self.rating + "]"

    def __len__(self):
        return

if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	pass
