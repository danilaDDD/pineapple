
try:
    from settings.local import DATABASES
except ImportError:
    print('not local')