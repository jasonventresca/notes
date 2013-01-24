# read this to understand generators / yield:
#   http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained

def create_items(label):
    print 'creating items for', label
    return [1, 2, 3, 4, 5]

def get_with_generator_expression():
    return (x for x in create_items('generator'))

def get_with_yield():
    for x in create_items('yield'):
        yield x

iter_gen = get_with_generator_expression()
iter_yield = get_with_yield()

