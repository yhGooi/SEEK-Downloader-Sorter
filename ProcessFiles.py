import os
import shutil

def move_files(d1, d2):
    shutil.move(d1, d2)
    return d2