from nautobot.extras.plugins import PluginConfig

__version__ = "1.0.0"

class NautobotPluginExampleConfig(PluginConfig):
    __module__ = "nautobot_plugin_example"  # Force root package module
    name = "nautobot_plugin_example"
    verbose_name = "nautobot_example_plugin"
    description = "Custom dashboard for device and KPI health."
    author = "Akhil"
    author_email = "shaikMohammed.AkhilTaj@gmail.com"
    required_settings = []
    default_settings = {}
    min_version = "1.0.0"
    max_version = "3.0.0"
    caching_config = {}

    urls = None  # disable URLs import

    def ready(self):
        super().ready()

