#Import Base-Plugin

from plugins import Base

#This is the main class. e.g. the GUI
class Main:
    def __init__(self):
        self.loaded_plugins={}  #The dict of Plugins: key: name of plugin, value: the plugin instance
        self.main_value = 0   # example value the main class

    def load_plugins(self):
        '''
        1. This function retrieves all classes that are available for Plugins.
        2. It creates an instance of each class and stores it into the loaded_plugins dict
        :return:
        '''
        for name, plugin in Base.plugins.items():
            print("Loading Plugin: {}".format(name))
            inst = plugin(self)  # create instance
            self.loaded_plugins[name] = inst

    def start_single_plugin(self, plg_name):
        '''
        Example on how to call a function of a plugin
        :param plg_name:
        :return:
        '''
        self.loaded_plugins[plg_name].start()

    def start_all_plugins(self):
        '''
        Example on how to call a function of all plugins
        :return:
        '''
        for name, plg in self.loaded_plugins.items():
            plg.start()

    def get_plugin(self,name):
        '''
        Example (Maybe useless) on how to get a instance of a plugin from outside this class
        :param name:
        :return:
        '''
        return self.loaded_plugins[name]


if __name__ == '__main__':
    '''
    Example Programm
    '''
    m=Main()
    m.load_plugins() #load all plugins (could also be called in constructor
    #print("Call PluginB")
    #m.start_single_plugin("PluginC")  #start a single plugin by name
    print("Call All")
    m.start_all_plugins()           #start all plugins
    #print("Main Counter value is: {}".format(m.main_value))
    #m.get_plugin("PluginA").set_main_value()    # call reimplemented function
    #print("New Main Counter value is: {}".format(m.main_value))
    #m.get_plugin("PluginB").set_main_value()    #call function of baseclass
    #print("New Main Counter value is: {}".format(m.main_value))
    #Call functions of plugins
    m.get_plugin("PluginB").plugin_b_function()
    #try:
    #    m.get_plugin("PluginA").plugin_b_function()
    #except Exception as e:
    #    print("Error:",e)

