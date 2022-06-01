import plugins


class PluginB(plugins.Base):
    def __init__(self,main):
        super().__init__(main)

    def start(self):
        print("Plugin B started")

    def plugin_b_function(self):
        print("Hello from B")