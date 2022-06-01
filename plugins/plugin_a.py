import plugins


class PluginA(plugins.Base):
    def __init__(self,main):
        super().__init__(main)

    def start(self):
        print("Plugin A started")

    def set_main_value(self):
        self.main_cls.main_value = 5
        print("Plugin A updates Main Counter to 5")