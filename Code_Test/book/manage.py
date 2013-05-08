#!/usr/bin/env python
import os
import sys

def setUpDjangoEnvironment():
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book.settings")
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)

if __name__ == "__main__":
	setUpDjangoEnvironment()
