def task_subtask():
    for i in ['heart', 'spleen', 'brain']:
        cmd = 'echo processing data from %s...' %i
        yield {
                'actions': [cmd],
                'name': 'subtask_%s' %i,
                }

def task_subtask_multi_commands():
    for i in ['heart', 'spleen', 'brain']:
        cmd1 = 'echo preprocessing data from %s...' %i
        cmd2 = 'echo analyzing data from %s...' %i
        yield {
                'actions': [cmd1, cmd2],
                'name': 'subtask_%s' %i,
                }
