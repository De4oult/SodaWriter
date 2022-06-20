from funcs import absolute, clear, comp

def compile(file):
    clear()
    comp(str('"' + absolute(file) + '"'))