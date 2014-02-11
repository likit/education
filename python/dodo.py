import os
import doit

def task_python_hello():
    print 'Hello from Python!'
    return {
            'actions':[''],
            'basename':'Python-hello',
            }

def task_shell_hello():
    return {
            'actions':['echo Hello from shell'],
            'basename':'Shell-hello',
            }

def task_python_hello_twice():
    def say_hello():
        for i in range(2):
            print 'hello! ',
        print
    return {
            'actions':[say_hello, ],
            'basename':'Python-hello-twice',
            }

def task_python_hello_times():
    def say_hello(times):
        for i in range(times):
            print 'hello! ',
        print
    return {
            'actions':[(say_hello, [5]), ],
            'basename':'Python-hello-%d-times' % 5,
            }

def task_shell_hello_target():
    return {
            'actions':['echo Hello from file > hello.txt'],
            'basename':'Shell-hello-target',
            'targets':['hello.txt'],
            }

def task_shell_hello_file():
    return {
            'actions':['cat hello.txt'],
            'basename':'Shell-hello-file',
            'file_dep':['hello.txt'],
            }

def task_shell_hello_target_in_sample_dir():
    if not os.path.exists('doit-sample'):
        os.mkdir('doit-sample')

    os.chdir('doit-sample')

    return {
            'actions':['echo Hello from file > hello.txt'],
            #'basename':'Shell-hello-target-in-sample',
            'targets':['doit-sample/hello.txt'],
            }
