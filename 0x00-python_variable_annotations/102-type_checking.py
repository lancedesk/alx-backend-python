#!/usr/bin/env python3
"""
Zoom array function
"""

from typing import List, Union


def zoom_array(lst: List, factor: Union[int, float] = 2) -> List:
    """
    Zoom in on the array by repeating each element by a given factor
    """
    zoomed_in = [
        item for item in lst
        for _ in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3.0)
