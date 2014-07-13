 #!/usr/bin/env python

import os
import sys

import dotenv

sys.path.insert(0, os.path.abspath('..'))

dotenv.read_dotenv()

if __name__ == "__main__":
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'DEVELOPMENT').title()

    os.environ.update(DJANGO_SETTINGS_MODULE='chatrooms.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', ENVIRONMENT)

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
