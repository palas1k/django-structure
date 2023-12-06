from core.core.utils.collections import deep_update
from core.core.utils.settings import get_settings_from_enviroment

# globals() is dictionary of global variables
# Takes env variables with a matching prefix, strips out the prefix and add its to global
deep_update(globals(), get_settings_from_enviroment(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
