print("load somepackage")
from .custom import checkSpec
from .custom import shout
__all__ = [
    'checkSpec',
    'shout'
]