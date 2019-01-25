import os
import datetime


def combine_file_path(instance, filename):
    return "game/static/game/image/{modelname}/{filename}".format(
        modelname=instance.__class__.__name__,
        filename=combine_filename_format(instance, filename)
    )


def combine_filename_format(instance, filename):
    now = datetime.datetime.now()
    return "{name}{extension}".format(
        name=instance.name,
        now=str(now.date()),
        extension=os.path.splitext(filename)[1],
    )

