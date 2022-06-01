import plugins


class PluginB(plugins.Base):
    def __init__(self,main):
        super().__init__(main)

    def start(self):
        print("Plugin B started")


    def update_main_cunter(self):
        self.main_cls.main_counter = 10
        print("Plugin B updates Main Counter to 10")