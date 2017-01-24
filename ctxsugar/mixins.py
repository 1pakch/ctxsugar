# mixins.py - the main context-providing and context-aware mixins

from stack import ContextStack
    

class ProvidesContext(object):

    "Provides context accessible from ContextAware objects"

    _stack = ContextStack()

    def __enter__(self):
        "Called on entering a `with` block using a class instance"
        self._stack.push(self)
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        "Called on the exit from the `with` block"
        self._stack.pop()


class ContextAware(object):

    "Has access to the current context"
    
    _stack = ProvidesContext._stack

    def __init__(self):
        "Pulls the current context from the stack"
        print 'sdfds'
        self.current_context = self._stack.top()

