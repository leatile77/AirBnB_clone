#!/usr/bin/python3
from models.engine.file_storage import FileStorage

"""Creates a unique FileStorage instance for application"""
storage = FileStorage()
storage.reload()
