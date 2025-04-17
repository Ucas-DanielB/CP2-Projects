import csv

# Load movie data into a list of dictionaries
movies = []

# Read data from 'movies.csv' file
with open('personal_portfolio\MoviesList.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Read the headers
    for row in reader:
        movies.append({
            'Title': row[0],
            'Director': row[1],
            'Genre': row[2],
            'Rating': row[3],
            'Length': int(row[4]),  # Convert length to integer
            'Actors': row[5:]  # Remaining values are actors
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
        filtered = [movie for movie in filtered if any(actor.lower() in map(str.lower, movie['Actors']) for actor in actors)]
    
    return filtered

# Function to print the movie list 
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
def main_4():
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
    main_4()
