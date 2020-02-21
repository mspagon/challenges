from collections import defaultdict

def count_competitors(reviews: list, competitors: list):
    # Initialize a dictionary with keys of all the competitor names whose values are set to 0.
    competitors_count = {k: 0 for k in competitors}
    for review in reviews:
        # Use a set to mark if a competitor was mentioned in the review so it is not counted more than once.
        seen = set()
        for word in review:
            if word in competitors_count:
                seen.add(word)

        for competitor in seen:
            competitors_count[competitor] += 1

    return sort_competitors(competitors_count)

def sort_competitors(competitors_count: dict):
    '''Sorts a dictionary of competitor counts and breaks ties alphabetically. Returns a list of competitor names.'''
    group_by_count = defaultdict(list)
    for competitor, count in competitors_count.items():
        group_by_count[count].append(competitor)

    competitors = []
    for count, competitor in sorted(group_by_count.items(), reverse=True):
        if count > 0:
            for name in sorted(competitor):
                competitors.append(name)
    return competitors


def tests():
    def _sort_competitors_simple():
        competitors_count = {
            'apple': 5,
            'samsung': 5,
            'samsungie': 5,
            'bapple': 5,
            'oranges': 3,
            'dogs': 3,
            'winner': 10,
            'weird': -1
        }
        answer = ['winner', 'apple', 'bapple', 'samsung', 'samsungie', 'dogs', 'oranges', 'weird']

        assert(sort_competitors(competitors_count) == answer)

    def _competitors_not_mentioned():
        reviews = ['blah blah blah', 'bloo bloo bloo']
        competitors = ['apple', 'samsung']
        answer = []

        try:
            assert(count_competitors(reviews, competitors) == answer)
        except:
            print(count_competitors(reviews, competitors))

    _sort_competitors_simple()
    _competitors_not_mentioned()


def main():
    reviews = [
        """cat apple hat dog fat man dog cat dog keyboard video
        apple vape candy super number alphabetical hat what an apple""",
        """samsung woot florida dog cat fat dog fat cat dog fat cat
        banana fat hat fat matt"""

    ]
    competitors = ['apple', 'samsung']

    print(count_competitors(reviews, competitors))

    tests()


if __name__ == '__main__':
    main()


