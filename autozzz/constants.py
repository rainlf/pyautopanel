"""
@author rain
@date 8/10/2024 10:38 AM
"""
import os


def _get_single_image(image):
    return os.path.join(FILE_DIR, 'image', image)


def _get_image(*images):
    ret = []
    for image in images:
        ret.append(_get_single_image(image))
    return ret


FILE_DIR = os.path.dirname(__file__)

# config
TASK_CONFIG = os.path.join(FILE_DIR, 'task.yaml')

# image
IMG_ME = _get_image('me.png', 'me2.png')
IMG_EXIT = _get_image('exit1.png', 'exit2.png')
IMG_HELP = _get_image('help1.png', 'help2.png', 'help3.png')
IMG_SURE = _get_image('sure.png')
IMG_COMPLETED = _get_image('completed.png')
IMG_GREEN = _get_single_image('green.png')
