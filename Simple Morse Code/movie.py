import csv

movies = []

movie_data = """Title,Director,Genre,Rating,Length (min),Notable Actors
The Shawshank Redemption,Frank Darabont,Drama,R,142,Tim Robbins, Morgan Freeman
Forrest Gump,Robert Zemeckis,Drama/Comedy,PG-13,142,Tom Hanks, Robin Wright
Back to the Future,Robert Zemeckis,Sci-Fi/Adventure,PG,116,Michael J. Fox, Christopher Lloyd
The Princess Bride,Rob Reiner,Adventure/Comedy,PG,98,Cary Elwes, Robin Wright
Jurassic Park,Steven Spielberg,Sci-Fi/Adventure,PG-13,127,Sam Neill, Laura Dern, Jeff Goldblum
E.T. the Extra-Terrestrial,Steven Spielberg,Sci-Fi/Family,PG,115,Henry Thomas, Drew Barrymore
The Lion King,Roger Allers, Rob Minkoff,Animation/Family,G,88,James Earl Jones, Matthew Broderick
Apollo 13,Ron Howard,Drama/History,PG,140,Tom Hanks, Kevin Bacon, Bill Paxton
Hidden Figures,Theodore Melfi,Drama/History,PG,127,Taraji P. Henson, Octavia Spencer, Janelle Monáe
The Martian,Ridley Scott,Sci-Fi/Drama,PG-13,144,Matt Damon, Jessica Chastain
Inception,Christopher Nolan,Sci-Fi/Action,PG-13,148,Leonardo DiCaprio, Joseph Gordon-Levitt
"""

reader = csv.DictReader(movie_data.strip().splitlines())
for row in reader:
    movies.append({
        'Title': row['Title'],
        'Director': row['Director'],
        'Genre': row['Genre'],
        'Rating': row['Rating'],
        'Length': int(row['Length (min)']),
        'Actors': row['Notable Actors'].split(', ')
    })

# Function to filter movies based on given criteria
def filter_movies(genre=None, director=None, length_min=None, actors=None):
    filtered = movies
    
    if genre:
        filtered = [movie for movie in filtered if genre.lower() in movie['Genre'].lower()]
    if director:
        filtered = [movie for movie in filtered if director.lower() in movie['Director'].lower()]
    if length_min:
        filtered = [movie for movie in filtered if movie['Length'] >= length_min]
    if actors:
        filtered = [movie for movie in filtered if any(actor.lower() in movie['Actors'] for actor in actors)]
    
    return filtered

# Function to print the movie list nicely
def print_movie_list(movie_list):
    if not movie_list:
        print("No movies found with the selected criteria.")
        return
    for movie in movie_list:
        print(f"Title: {movie['Title']}")
        print(f"Director: {movie['Director']}")
        print(f"Genre: {movie['Genre']}")
        print(f"Rating: {movie['Rating']}")
        print(f"Length: {movie['Length']} min")
        print(f"Notable Actors: {', '.join(movie['Actors'])}")
        print('-' * 40)

# Main menu
def main():
    while True:
        print("\nWelcome to the Movie Recommendation Program!")
        print("1. Print all movies")
        print("2. Filter movies")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            print_movie_list(movies)
        elif choice == '2':
            genre = input("Enter a genre to filter by (or leave blank): ")
            director = input("Enter a director to filter by (or leave blank): ")
            length_min = input("Enter minimum length in minutes (or leave blank): ")
            actors_input = input("Enter actors to filter by (comma separated, or leave blank): ")
            actors = [actor.strip() for actor in actors_input.split(',')] if actors_input else []

            # Handle the length input to convert to an integer if needed
            length_min = int(length_min) if length_min else None

            filtered_movies = filter_movies(genre, director, length_min, actors)
            print_movie_list(filtered_movies)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

# Run the program
if __name__ == "__main__":
    main()
