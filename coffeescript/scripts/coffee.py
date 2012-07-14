import console
import coffeescript
import optparse
import sys


def main():
    usage = "usage: %prog [source [destination]]"
    parser = optparse.OptionParser(usage=usage)
    (options, argv) = parser.parse_args()
    source = open(argv[0]) if len(argv) > 0 else sys.stdin
    destination = argv[1] if len(argv) > 1 else sys.stdout
    output = console.Writer(destination)
    output.write(coffeescript.compile(source.read()))
