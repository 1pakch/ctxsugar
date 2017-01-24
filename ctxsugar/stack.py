# stack.py - a stack for storing contexts and related exceptions

class ContextStackError(Exception):

    pass


class ContextStack(object):

    "A convenience class implementing a stack"

    def __init__(self, maxdepth=None):
        self._stack = []
        self.maxdepth = None

    def top(self):
        try:
            return self._stack[-1]
        except IndexError:
            raise ContextStackError('The context stack is empty')

    def push(self, context):
        if self.maxdepth is None or len(self._stack) < self.maxdepth:
            self._stack.append(context)
        else:
            raise ContextStackError(
                'Maximum stack depth %d is reached' % self.maxdepth)

    def pop(self):
        top = self.top()
        self._stack.pop()
        return top
