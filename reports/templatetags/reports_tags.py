from itertools import groupby

from django import template
from django.template.defaultfilters import stringfilter

from reports.num2word_ES import int_to_word

register = template.Library()


@register.filter
@stringfilter
def to_word(value, mode=""):
    """
    Attempts to convert any string into a wordy number. Non-digit characters
    will be let through. The noun arg will give numbers ending in 1 (that are
    not 11) a Spanish noun termination (add an 'o').
    """
    if mode.lower() == "adjective":
        noun_mode = False
    else:
        noun_mode = True
    tokens = ["".join(g) for k, g in groupby(str(value), key=str.isdigit)]
    for n, t in enumerate(tokens):
        if t.isdigit():
            tokens[n] = int_to_word(t, noun_mode)
    return " ".join(tokens)


@register.filter
@stringfilter
def gender_suffix(value):
    """
    Takes 'm' of 'f' as input and returns the correspondant termination.
    Currently only works in Spanish, but the locale should be autodetected
    and overridable via an optional argument.
    """
    suffix_dict = {"m": "o", "f": "a"}
    return suffix_dict.get(value)


@register.filter
@stringfilter
def lstrip(value, char=" "):
    """
    Wrapper for python's lstrip
    """
    char = str(char)
    return value.lstrip(char)
