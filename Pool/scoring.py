def read_score(file_name):
    """ Reads the score from a file.

    Args:
        file_name: A string which is the name of the file along with the file type.

    Returns:
        An integer of the read score.

        """
    score_file = open('high_score.txt', 'r')

    for line in score_file:

        score = line

    score = score.strip()
    score_file.close()
    return int(score)

prev_score = read_score('high_score.txt')

def write_score(file_name, score):
    """Writes score in the file

    Args:
        file_name: A string which is the name of the file along with the file type.
        score: An integer which is score of the game.
        """

    score_file = open('high_score.txt', 'w')
    score_file.write(str(score))
    score_file.close()