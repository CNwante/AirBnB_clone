#!/usr/bin/python3

"""
Creates a unique FIleStorage instance for my application

"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
