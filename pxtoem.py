#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def do_convert(unit, base, ignore_em):
    conv_type = unit[-2:].lower()

    if len(unit) < 3: return unit

    unit = unit[:-2]

    if not is_number(unit): return 'NaN'

    if conv_type == 'px':
        return str("%.2f" % round(float(unit) / base, 2)).rstrip('0.').lstrip('0') + 'em'
    elif not ignore_em:
        return str("%.2f" % round(float(unit) * base, 2)).rstrip('0.').lstrip('0') + 'px'
    else:
        return unit + conv_type


base = input('Enter base value in pixels: ')
base = int(base)

ignore_em = False if input('Ignore em inputs? [Y/n] ').lower() == 'n' else True
copy_result = False if input('Copy result to clipboard (require xsel)? [Y/n] ').lower() == 'n' else True

while True:
    unit = input('> ')
    if unit.lower() in ['q', 'exit']: exit()
    # We're dealing with list of values!
    if not " " in unit:
        # We'll default to 'px' if no unit provided,
        # but only in case of single value input.
        if is_number(unit) and unit != '0': unit = str(unit) + 'px'
        result = do_convert(unit, base, ignore_em)
    else:
        units = unit.split(' ')
        stack = []
        for unit in units:
            stack.append(do_convert(unit.strip(), base, ignore_em))
        result = ' '.join([str(item) for item in stack])

    print(result)
    if copy_result:
        p1 = subprocess.Popen(['echo', '-n', result], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["xsel", "-ib"], stdin=p1.stdout, stdout=subprocess.PIPE)
        p2.communicate()[0]