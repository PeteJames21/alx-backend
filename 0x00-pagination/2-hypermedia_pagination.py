#!/usr/bin/env python3
"""
Defines a class with:
- a method (get_page) for reading through the dataset page by page.
- a method (get_hyper) that wraps output from get_page() into a dict that has
  additional fields that give hypermedia pagination capabilities
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

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        Returns a data dict with hypermedia navigation fields.

        The returned dict has the following fields:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        start, end = self.index_range(page, page_size)

        # Get stats for the next page
        if (page < total_pages):
            next_page = page+1
        else:
            next_page = None

        # Get stats for the previous page
        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1

        return {'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
