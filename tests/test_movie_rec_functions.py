from source.movie_rec_functions import get_weighted_rating
import pytest
import pandas as pd

def test_get_weighted_rating():
	test_df = pd.DataFrame({'movie': ['1', '2', '3'],
							'vote_average':[8.7, 5.6, 7.9],
							'vote_count': [6000, 8000, 1000]})
	C = test_df['vote_average'].mean()
	m = 1000

	test_df['weighted_rating'] = get_weighted_rating(test_df, m = m, C = C)

	expected_output = pd.DataFrame({'movie': ['1', '2', '3'],
									'vote_average':[8.7, 5.6, 7.9],
									'vote_count': [6000, 8000, 1000],
									'weighted_rating': [8.51, 5.80, 7.65]})

	assert all(test_df == expected_output)
