#-----------------------------------------------#
# Below are functions used in the Movie         #
# Recommendation mini project                   #
#-----------------------------------------------#

def get_weighted_rating(x, m, C):
	R = x['vote_average']
	v = x['vote_count']

	WR = (v/(v+m)) * R + (m/(v+m)) * C

	return WR


if __name__ == '__main__':
	pass