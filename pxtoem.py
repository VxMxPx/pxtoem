#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess, sys, argparse

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def do_convert(unit, base, ignore):
    conv_type = unit[-2:].lower()

    if len(unit) < 3: return unit

    unit = unit[:-2]

    if not is_number(unit): return 'NaN'

    if conv_type == 'px':
        return str("%.2f" % round(float(unit) / base, 2)).rstrip('0').rstrip('.') + 'em'
    elif not ignore:
        return str("%.2f" % round(float(unit) * base, 2)).rstrip('0').rstrip('.') + 'px'
    else:
        return unit + conv_type


parser = argparse.ArgumentParser(prog='pxtoem', description='Simple command-line pixel to em (and vica versa) converter.')
parser.add_argument('base', default=16, type=int, help='Base numeric value (in px) which will be used for calculation')
parser.add_argument('-i', '--ignore', action='store_true', help='Ignore em units')
parser.add_argument('-c', '--copy', action='store_true', help='Copy result to clipboard (require xsel to be installed)')
opt = parser.parse_args(sys.argv[1:])

while True:
    unit = input('> ')
    if unit.lower() in ['q', 'exit']: exit()
    # We're dealing with list of values!
    if not " " in unit:
        # We'll default to 'px' if no unit provided,
        # but only in case of single value input.
        if is_number(unit) and unit != '0': unit = str(unit) + 'px'
        result = do_convert(unit, opt.base, opt.ignore)
    else:
        units = unit.split(' ')
        stack = []
        for unit in units:
            stack.append(do_convert(unit.strip(), opt.base, opt.ignore))
        result = ' '.join([str(item) for item in stack])

    print(result)
    if opt.copy:
        p1 = subprocess.Popen(['echo', '-n', result], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["xsel", "-ib"], stdin=p1.stdout, stdout=subprocess.PIPE)
        p2.communicate()[0]
