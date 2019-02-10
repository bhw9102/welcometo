import os
import datetime


def combine_file_path(instance, filename):
    return "{modelname}/{filename}".format(
        modelname=instance.__class__.__name__,
        filename=combine_filename_format(instance, filename)
    )


def combine_filename_format(instance, filename):
    return "{name}{extension}".format(
        name=instance.name,
        extension=os.path.splitext(filename)[1],
    )

