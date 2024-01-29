#!/usr/bin/env python3
"""
A simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two start and end indexes
    for the given pagination parameters.
    """
    start = page * page_size - page_size
    end = start + page_size
    return (start, end)
