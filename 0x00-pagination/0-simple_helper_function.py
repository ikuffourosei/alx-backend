#!/usr/bin/env python3
'''A simple helper function for pagination'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters."""
    start_ind = (page - 1) * page_size
    end_ind = page * page_size
    result = (start_ind, end_ind)
    return result
