from django.test import TestCase

# Create your tests here.
from django.db import models

# Create your moddels

# phone = input('> ')


def converterSmiley(words):
    words = phone.split(' ')
    list_mapping = {
        ':(': '😢',
        ':)': '😄',
    }
    output = ''
    for item in words:
        output += list_mapping.get(item, item)+' '
    return output


# print(converterSmiley(words=phone))
