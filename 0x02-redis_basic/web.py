#!/usr/bin/env python3
""" implementing an expiring web cache tracker """


def get_page(url: str) -> str:
    """ get HTTP content of URL and return it """
