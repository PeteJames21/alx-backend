#!/usr/bin/env python3
"""
Defines a helper function for defining start and end indexes in
offset pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indices for the specified page."""

    return ((page-1) * page_size, page_size * page)
