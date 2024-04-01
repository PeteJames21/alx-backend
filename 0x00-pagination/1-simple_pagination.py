#!/usr/bin/env python3
"""
Defines a class with a method for reading through the dataset
page by page.
"""


import csv
import math
from typing import List, Tuple


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Read the CSV file into memory.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Return the start and end indices for the specified page."""
        # Pages are counted from 1, not 0

        return ((page-1) * page_size, page_size * page)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve data from a specific page."""
        # Verify that both arg are integers greater than zero.
        assert all(type(arg) is int and arg > 0 for arg in (page, page_size))

        # Get page indices
        start, end = self.index_range(page, page_size)

        # Return page data
        try:
            return self.dataset()[start: end]
        except IndexError:
            return []
