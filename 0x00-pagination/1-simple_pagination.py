#!/usr/bin/env python3
"""Simple Pagination"""


import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) == int, 'page must be an integer'
        assert type(page_size) == int, 'page_size must be an integer'
        assert page > 0, 'page must be greater than 0'
        assert page_size > 0, 'page_size must be greater than 0'
        data = self.dataset()
        pages = index_range(page, page_size)
        start, end = pages
        if start >= len(data):
            return []
        result = data[start: end]
        return result


def index_range(page: int, page_size: int) -> Tuple:
    """Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters."""
    start_ind = (page - 1) * page_size
    end_ind = page * page_size
    result = (start_ind, end_ind)
    return result
