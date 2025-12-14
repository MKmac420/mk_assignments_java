import pandas

def generate_recommendations(movies_filepath, user_ratings_filepath, like_threshold=8.0):
    """
    Generates movie recommendations for a user based on their ratings.
    This version reads directly from CSV file paths.
    """
    # Part A: load and prepare data from input
    try:
        movies_df = pandas.read_csv(movies_filepath)
        user_df = pandas.read_csv(user_ratings_filepath)
    except FileNotFoundError:
        print(f"Error: One of the files was not found. Please ensure '{movies_filepath}' and '{user_ratings_filepath}' exist.")
        return []

    # Part B: discretize IMDB ratings
    rating_bins = [0, 3.9, 6.9, 10]
    rating_labels = ['Low Tier', 'Mid Tier', 'High Tier']
    movies_df['rating_tier'] = pandas.cut(movies_df['imdb_rating'], bins=rating_bins, labels=rating_labels)

    # Part C: learn user interests
    user_profile_df = pandas.merge(user_df, movies_df, on='movie_name')
    
    p_genre_interest = user_profile_df['genre'].value_counts(normalize=True).to_dict()
    p_lang_interest = user_profile_df['language'].value_counts(normalize=True).to_dict()
    p_tier_interest = user_profile_df['rating_tier'].value_counts(normalize=True).to_dict()

    # part D: score Unseen Movies
    unseen_movies = movies_df[~movies_df['movie_name'].isin(user_df['movie_name'])]
    recommendations = []

    for _, movie in unseen_movies.iterrows():
        genre = movie['genre']
        language = movie['language']
        tier = movie['rating_tier']
        
        p_genre = p_genre_interest.get(genre, 0.01)
        p_lang = p_lang_interest.get(language, 0.01)
        p_tier = p_tier_interest.get(tier, 0.01)

        score = p_genre * p_lang * p_tier # Naive bayes
        recommendations.append({'movie_name': movie['movie_name'], 'score': score})

    # Part E: Return the final list
    return sorted(recommendations, key=lambda x: x['score'], reverse=True)

# the following code will be called for the function to execute and return the recomendation data

movie_database_filepath = 'movie_database.csv'
user_a_ratings_filepath = 'user_a_ratings.csv'

# generate and print the recommendations for User A
recommendations_for_user_a = generate_recommendations(movie_database_filepath, user_a_ratings_filepath)

print("--- Recommendations for User A ---")
if recommendations_for_user_a:
    for movie in recommendations_for_user_a[:5]:
        print(f"- {movie['movie_name']} (Score: {movie['score']:.4f})")
else:
    print("an error occured, please ensure that both csv files are in the same folder as the python file, thank you")
