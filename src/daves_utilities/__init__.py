"""
Daves utilities is a collection of useful python functions which I would like to
provide to anybody who is interested in using them.
"""
from daves_utilities.archive.fun_save import fun_save
from daves_utilities.archive.is_equal import is_equal
from daves_utilities.archive.print_structure import print_structure
from daves_utilities.david_secrets import decrypt_message
from daves_utilities.david_secrets import encrypt_message
from daves_utilities.david_secrets import generate_key
from daves_utilities.iterator import for_long

__all__ = [
    "for_long",
    "fun_save",
    "is_equal",
    "print_str",
    "print_structure",
    "decrypt_message",
    "encrypt_message",
    "generate_key",
]
