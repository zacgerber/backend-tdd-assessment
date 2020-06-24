#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "???"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument('text', help="text to echo")
    parser.add_argument('-u', '--upper', action="store_true", help="convert text to uppercase")
    parser.add_argument('-l', '--lower', action="store_true", help="convert text to lowercase")
    parser.add_argument('-t', '--title', action="store_true", help="convert text to titlecase")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args(args)

    msg = args.text
    if args.upper:
        msg = msg.upper()
    if args.lower:
        msg = msg.lower()
    if args.title:
        msg = msg.title()

    print(msg)


if __name__ == '__main__':
    main(sys.argv[1:])
