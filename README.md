pxtoem
======

usage: pxtoem [-h] [-i] [-c] base

Simple command-line pixel to em (and vica versa) converter.

positional arguments:
  base          Base numeric value (in px) which will be used for calculation

optional arguments:
  -h, --help    show this help message and exit
  -i, --ignore  Ignore em units
  -c, --copy    Copy result to clipboard (require xsel to be installed)

## Examples

To enter interactive mode, use:

    ./pxtoem.py 16

The above example will assume 16(px) to be a base value, and make all calculations based on it.
In interactive mode, enter desired values, for example:

    in  > 1200px
    out < 75em

    in  > 75em
    out < 1200px
