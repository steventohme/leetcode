class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        pass
    def peek(self) -> int:
        pass

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.peek)