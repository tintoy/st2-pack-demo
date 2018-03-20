from st2common.runners.base_action import Action

class Greet2(Action):
    '''
    Simple Python-based action that greets the caller.
    '''

    def run(self, name):
        greeting = 'Hello, {0}'.format(name)
        print(greeting)

        if name.lower().startswith('a'):
            return (True, greeting)
        else:
            return (False, greeting)
