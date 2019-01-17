#!/usr/bin/env python3
import argparse


__VERSION__ = '0.1.0'


def bootstrapper():
    parser = argparse.ArgumentParser(
        description="la Campana: Notify you when complete executing a command"
    )
    sub_parsers = parser.add_subparsers()

    # campana add
    campana_add = sub_parsers.add_parser(
        'add',
        help='Add a notification setting'
    )
    campana_add.add_argument(
        'alias',
        help='A short name for this setting.'
    )
    campana_add.add_argument(
        'notification-setting-string',
        help='Example: "email:me@foo.bar"'
    )
    campana_add.set_defaults(func=aggiungere)

    # campana list
    campana_list = sub_parsers.add_parser(
        'list', aliases=['ls'],
        help='List all notification settings'
    )
    campana_list.set_defaults(func=elencare)

    # campana remove
    campana_remove = sub_parsers.add_parser(
        'remove', aliases=['rm'],
        help='Remove a notification setting'
    )
    campana_remove.add_argument(
        'setting',
        help='Short name of the notification setting'
    )
    campana_remove.set_defaults(func=annullare)

    # campana ring
    campana_ring = sub_parsers.add_parser(
        'ring',
        help='Run a command and get notified when completed'
    )
    campana_ring.add_argument(
        'setting',
        help='Short name of the notification setting'
    )
    campana_ring.add_argument(
        'command',
        help='Command to run'
    )
    campana_ring.set_defaults(func=suonare)

    # parse
    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.print_help()
        exit(0)


def aggiungere(args):
    pass


def elencare(args):
    pass


def annullare(args):
    pass


def suonare(args):
    pass


if __name__ == '__main__':
    bootstrapper()
