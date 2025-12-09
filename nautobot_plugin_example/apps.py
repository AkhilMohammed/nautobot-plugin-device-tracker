from nautobot.apps import NautobotAppConfig


__version__ = "1.0.0"


class NautobotPluginExampleConfig(NautobotAppConfig):
    name = "nautobot_plugin_example"
    verbose_name = "nautobot_example_plugin"
    version = __version__
    description = "Custom dashboard for device and KPI health."
    author = "Akhil"
    author_email = "shaikMohammed.AkhilTaj@gmail.com"

    required_settings = []
    default_settings = {}
    min_version = "1.0.0"
    max_version = "3.0.0"
    caching_config = {}

    def ready(self):
        super().ready()

