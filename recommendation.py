# Author: Nishant Garg
# Project: CodSoft AI Internship Task 4
# Description: Movie Recommendation System using content-based filtering
# Language: Python

# Sample movie data
movies = {
    "Interstellar": ["sci-fi", "space", "future", "drama"],
    "Inception": ["dream", "action", "thriller", "sci-fi"],
    "The Dark Knight": ["action", "crime", "hero", "thriller"],
    "Tenet": ["time", "sci-fi", "action", "mind-bending"],
    "Gravity": ["space", "survival", "drama", "sci-fi"],
    "Avengers": ["superhero", "action", "team", "marvel"],
    "Iron Man": ["technology", "marvel", "action", "superhero"]
}

def get_recommendations(selected_movie):
    if selected_movie not in movies:
        return "Movie not found in database."

    selected_tags = set(movies[selected_movie])
    recommendations = []

    for movie, tags in movies.items():
        if movie == selected_movie:
            continue
        similarity = len(selected_tags.intersection(tags))
        recommendations.append((movie, similarity))

    # Sort by similarity score (descending)
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return [movie for movie, score in recommendations if score > 0]

# Program starts here
print("🎬 Welcome to the Movie Recommender!")
print("Available movies:", ", ".join(movies.keys()))
user_input = input("Enter a movie you like: ")

suggestions = get_recommendations(user_input)

if isinstance(suggestions, str):
    print(suggestions)
else:
    print("\nBecause you liked", user_input)
    print("You might also like:")
    for movie in suggestions:
        print("✅", movie)