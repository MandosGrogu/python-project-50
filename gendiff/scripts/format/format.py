from gendiff.scripts.format.json_formater import json_formatter
from gendiff.scripts.format.plain_formater import plain_formatter
from gendiff.scripts.format.stylish_formater import stylish_formatter


def format_diff(diff, format_name):

    if format_name == 'stylish':
        formatted_str = stylish_formatter(diff)
    elif format_name == 'plain':
        formatted_str = plain_formatter(diff)
    elif format_name == 'json':
        formatted_str = json_formatter(diff)

    return formatted_str