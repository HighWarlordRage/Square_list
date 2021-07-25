#title: Project-7a
def square_list(lon):
    """A that takes as a parameter a list of numbers and
    replaces each value with the square of that value """
    for m in range(len(lon)):
        lon[m] = lon[m] * lon[m]
#nums = [7, -3, 12, 9]
#square_list(nums)
#print(nums)  # This should print [49, 9, 144, 81]