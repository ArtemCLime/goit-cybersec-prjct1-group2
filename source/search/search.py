import difflib


def search(query, data, top_n=3):
    """
    Search for a query in the data.
    """
    return difflib.get_close_matches(query, data, n=top_n, cutoff=0.2)
