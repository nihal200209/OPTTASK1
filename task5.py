import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

# Example data: user-item interaction matrix
# Rows represent users, columns represent items, values are interactions (views, purchases)
user_item_matrix = np.array([
    [5, 0, 3, 0],
    [4, 0, 4, 3],
    [1, 1, 0, 0],
    [0, 0, 5, 4],
])

# Decompose the user-item matrix using SVD
svd = TruncatedSVD(n_components=2)
matrix_factorization = svd.fit_transform(user_item_matrix)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(matrix_factorization)

# Recommend items based on user similarities
def recommend_items(user_index, user_similarity, user_item_matrix, top_n=2):
    similar_users = user_similarity[user_index].argsort()[::-1][1:]  # Exclude the user itself
    recommendations = []

    for similar_user in similar_users:
        user_interactions = user_item_matrix[similar_user]
        for i, interaction in enumerate(user_interactions):
            if interaction > 0 and user_item_matrix[user_index, i] == 0:
                recommendations.append(i)
            if len(recommendations) >= top_n:
                break
        if len(recommendations) >= top_n:
            break

    return recommendations

# Get recommendations for user 0
user_index = 0
recommended_items = recommend_items(user_index, user_similarity, user_item_matrix)

print(f"Recommended items for user {user_index}: {recommended_items}")
