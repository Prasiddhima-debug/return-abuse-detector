import yaml

# YAML file path
yaml_file = "openenv.yaml"

# Load YAML
with open(yaml_file, "r") as f:
    data = yaml.safe_load(f)

# Pretty print
import pprint
pprint.pprint(data)