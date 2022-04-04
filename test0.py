import yaml
import sys

# Load YAML data from the file
with open('file1.yaml') as fh:
    read_data = yaml.load(fh, Loader=yaml.FullLoader)
# Print YAML data before sorting
print(read_data)

