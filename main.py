from plugins import Base

class Main:

    def __init__(self):
        self.loaded_plugins={}
        self.main_counter = 0
    def load_plugins(self):
        for name,plg in Base.plugins.items():
            print("Loading Plugin: {}".format(name))
            inst = plg(self)
            self.loaded_plugins[name] = inst

    def call_single_plugin(self,plg_name):
        self.loaded_plugins[plg_name].start()

    def call_all_plugins(self):
        for name, plg in self.loaded_plugins.items():
            plg.start()

    def get_plugin(self,name):
        return self.loaded_plugins[name]



if __name__ == '__main__':
    m=Main()
    m.load_plugins()
    print("Call PluginB")
    m.call_single_plugin("PluginB")
    print("Call All")
    m.call_all_plugins()
    print("Main Counter value is: {}".format(m.main_counter))
    m.get_plugin("PluginA").update_main_cunter()
    print("New Main Counter value is: {}".format(m.main_counter))
    m.get_plugin("PluginB").update_main_cunter()
    print("New Main Counter value is: {}".format(m.main_counter))
