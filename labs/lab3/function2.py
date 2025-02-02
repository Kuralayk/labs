def is_high_rated(movie):
    return movie["imdb"] > 5.5
def high_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]
def movies_by_category(movies, category_name):
    return [movie for movie in movies if movie["category"] == category_name]
def average_imdb_score(movies):
    if len(movies) == 0:
        return 0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)
def average_imdb_by_category(movies, category_name):
    category_movies = movies_by_category(movies, category_name)
    return average_imdb_score(category_movies)

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]


#1
for movie in movies:
    print(f"{movie['name']} has a high rating: {is_high_rated(movie)}")
#2
high_rated = high_rated_movies(movies)
print("High rated movies:", [movie["name"] for movie in high_rated])

#3
romance_movies = movies_by_category(movies, "Romance")
print("Romance movies:", [movie["name"] for movie in romance_movies])

#4
avg_score = average_imdb_score(movies)
print("Average IMDB score:", avg_score)

#5
avg_romance_score = average_imdb_by_category(movies, "Romance")
print("Average IMDB score for Romance movies:", avg_romance_score)
