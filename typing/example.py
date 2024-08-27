# https://gist.github.com/inaz2/d436e4273e4f3051dcbd7b7d990d408e

import requests


def ident(x):
    return x


def add_1(x):
    return x + 1


def and_y(x, y):
    return x and y


def or_y(x, y):
    return x or y


def implicit_none(x):
    if x:
        return x


def list_any_unannotated():
    lst = ["PyCon"]
    lst.append(2019)
    return [str(x) for x in lst]


def list_any_annotated() -> list[str]:
    lst = ["PyCon"]
    lst.append(2019)
    return [str(x) for x in lst]


def third_party_module():
    r = requests.get("/api/users/profile")
    return r.status_code


def test():
    add_1("str").upper()
    add_1(ident("str")).upper()
    and_y("str", 1).upper()
    or_y(1, "str").upper()
    implicit_none("").upper()
    list_any_unannotated()
    list_any_annotated()
    third_party_module().upper()
