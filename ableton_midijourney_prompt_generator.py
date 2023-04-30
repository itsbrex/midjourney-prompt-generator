# This script generates a random prompt for the Ableton Midi Journey project.
import random
import yaml

# style:
#   - modern
#   - minimalist
#   - vintage
#   - retro
#   - 80s
#   - futuristic
#   - abstract
#   - geometric

def get_options(file_path):
    with open(file_path, 'r') as file:
        options = yaml.load(file, Loader=yaml.FullLoader)
    return options

input_data = get_options('input.yaml')

styles = input_data['style']
style_indices = list(range(len(styles)))

for i in range(20):
    if len(style_indices) == 0:
        style_indices = list(range(len(styles)))
    # Select a random style index and remove it from the list of available indices
    style_index = style_indices.pop(random.randint(0, len(style_indices) - 1))
    style = styles[style_index]

    # Build the command using the selected style
    command = input_data['command']
    for key in input_data.keys():
        if key != 'command' and key != 'style':
            command = command.replace(f'[{key}]', str(input_data[key][random.randint(0, len(input_data[key]) - 1)]))
    command = command.replace('[styles]', style)

    # Add options to the end of the command
    command += ' --v 5 --ar 16:9 --c 20 --q 0.5'

    # Print the command
    print(command)