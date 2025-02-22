from typing import Dict, List
from django.http import HttpRequest


def menu_items_processor(request: HttpRequest) -> Dict[str, List[Dict[str, str]]]:
    """
    A Django context processor that returns the menu items as a list of dictionaries.

    The request object is not used in this processor, but it is required as an argument
    by Django.

    Returns a dictionary with a single key, "menu_items", which is a list of dictionaries
    with the following keys:

    - url_name: The URL name of the menu item.
    - label: The human-readable label of the menu item.
    """
    return {
        "menu_items": [
            {"url_name": "artists", "label": "ARTISTS"},
            {"url_name": "releases", "label": "RELEASES"},
            {"url_name": "events", "label": "EVENTS"},
            {"url_name": "podcast", "label": "PODCAST"},
        ]
    }
