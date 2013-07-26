#!/usr/bin/env python
# -*- coding: utf-8 -*-
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def do_convert(unit, conversion, conv_type):
    if not is_number(unit): return 'Not a valid number!'
    if conv_type == 'px':
        return str("%.2f" % round(float(unit) / conversion, 2)).rstrip('0.').lstrip('0') + 'em'
    else:
        return str("%.2f" % round(float(unit) * conversion, 2)).rstrip('0.').lstrip('0') + 'px'

base = input('Enter base value [npx | nem]: ')
conv_type = base[-2:].lower()
conversion = int(base[:-2])

if conv_type != 'px' and conv_type != 'em':
    print('Invalid value entered. Must end with px or em.')
    exit()

while True:
    unit = input(('em' if conv_type == 'px' else 'px') + '> ')
    if unit.lower() in ['q', 'exit']: exit()
    # We're dealing with list of values!
    if not " " in unit:
        print(do_convert(unit, conversion, conv_type))
    else:
        units = unit.split(' ')
        stack = []
        for unit in units:
            stack.append(do_convert(unit.strip(), conversion, conv_type))
        print(' '.join([str(item) for item in stack]))
