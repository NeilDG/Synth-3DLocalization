import global_config

class ConfigHolder():
    _sharedInstance = None

    @staticmethod
    def initialize(yaml_data, hyperparam_data):
        if(ConfigHolder._sharedInstance == None):
            ConfigHolder._sharedInstance = ConfigHolder(yaml_data, hyperparam_data)

    @staticmethod
    def getInstance():
        return ConfigHolder._sharedInstance

    def __init__(self, yaml_data, hyperparam_data):
        self.yaml_config = yaml_data
        self.hyperparam_config = hyperparam_data

    def get_network_config(self):
        return self.yaml_config

    def get_network_attribute(self, key, default):
        if(key in self.yaml_config):
            # print("Key ", key, " found. Returning ", self.yaml_config[key])
            return self.yaml_config[key]
        else:
            return default

    def get_hyper_params(self):
        return self.hyperparam_config

    def get_hyper_params_weight(self, iteration, key):
        hyperparams_table = self.hyperparam_config["hyperparams"][iteration]
        if(key in hyperparams_table):
            return hyperparams_table[key]
        else:
            return 0.0

    def get_version_name(self):
        general_config = global_config.general_config
        network_version = general_config["network_version"]
        iteration = general_config["iteration"]

        return str(network_version) + "_" + str(iteration)