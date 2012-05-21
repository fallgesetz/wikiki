class WikikiPlugin(object):
    """
        Interface for all plugins
    """
    __metaclass__ = PluginManager
    pass

class PluginManager(type):
    plugins = []
    def __new__(klass, classname, bases, class_dict):
        if not issubclass(classname, WikikiPlugin):
            raise TypeError("%s is not of type WikikiPlugin")
        plugins.append(classname)
        return type.__new__(meta, classname, bases, class_dict)

    def get_plugins():
        return plugins
