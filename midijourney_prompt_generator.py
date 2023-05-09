import random
import yaml
import datetime
import os

def get_options(file_path):
    with open(file_path, 'r') as file:
        options = yaml.load(file, Loader=yaml.FullLoader)
    return options

def generate_command(input_data, style_indices):
    styles = input_data['style']
    if len(style_indices) == 0:
        style_indices = list(range(len(styles)))
    style_index = style_indices.pop(random.randint(0, len(style_indices) - 1))
    style = styles[style_index]

    command = input_data['command']
    for key in input_data.keys():
        if key != 'command' and key != 'style':
            command = command.replace(f'[{key}]', str(input_data[key][random.randint(0, len(input_data[key]) - 1)]))
    command = command.replace('[styles]', style)
    command += ' --v 5 --ar 16:9 --c 20 --q 1'

    return command, style_indices

input_data = get_options('input.yaml')
styles = input_data['style']
style_indices = list(range(len(styles)))

commands = []
for _ in range(20):
    command, style_indices = generate_command(input_data, style_indices)
    commands.append(command)
    print(command)

# Create the 'prompts' directory if it doesn't exist
if not os.path.exists('prompts'):
    os.makedirs('prompts')

timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
with open(os.path.join('prompts', f'output_{timestamp}.txt'), 'w') as file:
    for command in commands:
        file.write(command + '\n')
