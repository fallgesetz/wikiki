class WikikiPlugin(object):
    __metaclass__ = PluginManager
    """
    To modify how a particular wiki key is rendered, define render_<key> as a function.
    For example,

    def render_link(content):
        # do some stuff to content
        return blah

    The signature for these functions is the same as for render
    """
    def render(content):
        """
        General rendering function for a key/value page,
        called if a specific function is not defined
        Parameters
        ----------
        content: raw data from the kv store

        Returns
        -------
        parsed/tokenize/finagled data
        """
        raise NotImplementedError

class PluginManager(type):
    plugins = []
    def __new__(klass, classname, bases, class_dict):
        if not issubclass(classname, WikikiPlugin):
            raise TypeError("%s is not of type WikikiPlugin")
        plugins.append(classname)
        return type.__new__(meta, classname, bases, class_dict)

    def get_plugins():
        return plugins
