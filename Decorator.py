class UppercaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result.upper()

@UppercaseDecorator
def print_message():
    return "heLlo woRld"

print(print_message())