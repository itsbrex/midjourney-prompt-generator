import random
import yaml


def get_options(file_path):
    with open(file_path, 'r') as file:
        options = yaml.load(file, Loader=yaml.FullLoader)
    return options

input_data = get_options('input.yaml')

command = input_data['command']
for key in input_data.keys():
    if key != 'command':
        command = command.replace(f'[{key}]', input_data[key][random.randint(0, len(input_data[key]) - 1)])

print(command)
# # output to file
# with open('output.md', 'w') as file:
#     file.write(command)