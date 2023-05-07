class Movie:
    ''' This program illustrates OOP concept using Python'''

    def __init__(self, title, cast):
        self.title = title
        self.cast = cast

    def info(self):
        print("Movie name is:", self.title)
        print("Cast is:", self.cast)


list_of_movies = []
while (True):
    title = input('Enter movie name:')
    cast = input('Enter cast name:')
    movie_ref = Movie(title, cast)
    list_of_movies.append(movie_ref)
    print("Movie and cast added successfully.")

    option = input('Do you want to add more movie (Y/N):')
    if option.lower() == 'n':
        break

print("All Movies information")
for m in list_of_movies:
    m.info()
    print()
