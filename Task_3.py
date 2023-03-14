files = {
    'cool_movie.avi': ['X'],
    'math_summary.docx': ['R', 'W'],
    'war_and_peace.txt': ['R', 'W', 'X']
}
possible_commands = {
    'read': 'R',
    'write': 'W',
    'execute': 'X'
}


def action(command):
    splitted_command = command.split(' ')
    possible_actions = files.get(splitted_command[1])
    wanted_action = possible_commands.get(splitted_command[0])
    if wanted_action in possible_actions:
        print('OK')
    else:
        print('Access denied')


action('write cool_movie.avi')
action('execute cool_movie.avi')
