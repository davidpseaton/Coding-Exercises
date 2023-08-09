def display():
    print("This is a message")

def decorator(display_fn):
    print("Display function :") 
    display_fn()

decorator(display)

