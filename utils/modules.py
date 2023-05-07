from django.utils.deconstruct import deconstructible
from uuid import uuid4
import os

from online_shop import settings


@deconstructible
class path_and_rename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


def get_message(message_key):
    if message_key is not None and message_key != "":
        if message_key in settings.MESSAGES_FILE:
            if settings.DEFAULT_LOCALE in settings.MESSAGES_FILE[message_key]:
                return settings.MESSAGES_FILE[message_key][settings.DEFAULT_LOCALE]
    return ""
