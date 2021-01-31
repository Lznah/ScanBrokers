import os

def set_envvar(ENVVAR_NAME, value):
    os.environ[ENVVAR_NAME] = value

def del_envvar(ENVVAR_NAME):
    del os.environ[ENVVAR_NAME]