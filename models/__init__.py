#!/usr/bin/python3
"""initialize the packages"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()