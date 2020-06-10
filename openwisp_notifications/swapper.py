from openwisp_notifications.apps import OpenwispNotificationsConfig as AppConfig
from swapper import load_model as swapper_load_model


def load_model(model):
    return swapper_load_model(AppConfig.label, model)
