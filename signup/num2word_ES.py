#! /usr/bin/env python
# -*- coding: utf-8 -*-

UNIDADES = (
    '',
    'un',
    'dos',
    'tres',
    'cuatro',
    'cinco',
    'seis',
    'siete',
    'ocho',
    'nueve',
    'diez',
    'once',
    'doce',
    'trece',
    'catorce',
    'quince',
    'dieciseis',
    'diecisiete',
    'dieciocho',
    'diecinueve',
    'veinte '
)

DECENAS = (
    'veinti',
    'treinta',
    'cuarenta',
    'cincuenta',
    'sesenta',
    'setenta',
    'ochenta',
    'noventa',
    'cien'
)

CENTENAS = (
    'ciento',
    'doscientos',
    'trescientos',
    'cuatrocientos',
    'quinientos',
    'seiscientos',
    'setecientos',
    'ochocientos',
    'novecientos'
)


def int_to_word(number, noun=False):
    """
    Converts an number to its 'wordy' representation. Handles leading zeros
    before performing the actual convertion.
    """
    converted = ''
    no_zeros = number.lstrip("0")
    zero_count = len(number) - len(no_zeros)
    converted += "cero " * zero_count

    if no_zeros != '' and not (0 < int(no_zeros) < 999999999):
        return "Can't convert"

    number_str = no_zeros.zfill(9)
    millions = number_str[:3]
    thousands = number_str[3:6]
    hundreds = number_str[6:]

    if(millions):
        if(millions == '001'):
            converted += 'un millón'
        elif(int(millions) > 0):
            converted += '%s millones' % __convert_group(millions)

    if(thousands):
        if(thousands == '001'):
            converted += ' mil'
        elif(int(thousands) > 0):
            converted += ' %s mil' % __convert_group(thousands)

    if(hundreds):
        if(hundreds == '001'):
            converted += ' un'
        elif(int(hundreds) > 0):
            converted += ' %s' % __convert_group(hundreds)
        if hundreds[2] == '1' and hundreds[1:] != '11' and noun:
            converted += 'o'

    return " ".join(converted.split())  # Get rid of multiple whitespace


def __convert_group(n):
    """Turn each group of numbers into letters"""
    output = ''

    if(n == '100'):
        output = "cien"
    elif(n[0] != '0'):
        output = CENTENAS[int(n[0]) - 1] + " "

    k = int(n[1:])
    if(k <= 20):
        output += UNIDADES[k]
    else:
        if((k > 30) & (n[2] != '0')):
            output += '%s y %s' % (DECENAS[int(n[1]) - 2], UNIDADES[int(n[2])])
        else:
            output += '%s%s' % (DECENAS[int(n[1]) - 2], UNIDADES[int(n[2])])

    return output
