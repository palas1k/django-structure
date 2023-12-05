import os

from .misc import yaml_coerce




def get_settings_from_enviroment(prefix):
    '''
    делает такие действия
        'CORESETTINGS_IN_DOCKER = 1'
    {
        'IN_DOCKER':1
    }
    '''
    prefix_len = len(prefix)
    return {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
