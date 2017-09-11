from link import *
from tree import *
from stream import *

## Linked Lists
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print_link(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print_link(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print_link(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty or Link.rest is Link.empty:
        return 
    if link.rest.first == value:
        link.rest = link.rest.rest
        remove_all(link, value)
    else:
        remove_all(link.rest, value)


## Trees
def reverse_other(t):
    """Reverse the entries of every other level of the tree using mutation.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(5, [Tree(7), Tree(8)]), Tree(6)]), Tree(3)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5, [Tree(8), Tree(7)]), Tree(6)]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"

## Object_Oriented Programming
class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2017
    >>> dime = mint.create(Dime)
    >>> dime.year
    2017
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2017
    >>> nickel.worth()  # 5 cents + (85 - 50 years)
    38
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (160 - 50 years)
    118
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (160 - 50 years)
    128

    """
    current_year = 2017

    def __init__(self):
        self.update()

    def create(self, kind):
        "*** YOUR CODE HERE ***"

    def update(self):
        "*** YOUR CODE HERE ***"

class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10

## Iterators and Generators
class Str:
    """
    >>> s = Str("hello")
    >>> for char in s:
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    >>> for char in s:    # a standard iterator does not restart
    ...     print(char)
    """
    "*** YOUR CODE HERE ***"

class ListDictIter:
    """ Returns an iterator that yields either the corresponding 
    dictionary value of the next element in the list or the element
    itself if it is not a key in the dictionary.

    >>> sounds = {'cat': 'meow', 'cow': 'moo','ghost': 'boo'}
    >>> things = ['cat', 'moo', 'ghost', 'pikachu']
    >>> x = ListDictIter(things, sounds)
    >>> list(x)
    ['meow', 'moo', 'boo', 'pikachu']
    >>> y = ListDictIter(things, sounds)
    >>> next(y)
    'meow'
    >>> next(y)
    'moo'
    """

    def __init__(self, lst, dct):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        return self

    def __next__(self):
        "*** YOUR CODE HERE ***"

def pairs(lst):
    """
    >>> type(pairs([3, 4, 5]))
    <class 'generator'>
    >>> for x, y in pairs([3, 4, 5]):
    ...     print(x, y)
    ...
    3 3
    3 4
    3 5
    4 3
    4 4
    4 5
    5 3
    5 4
    5 5
    """
    "*** YOUR CODE HERE ***"

class PairsIterator:
    """
    >>> for x, y in PairsIterator([3, 4, 5]):
    ...     print(x, y)
    ...
    3 3
    3 4
    3 5
    4 3
    4 4
    4 5
    5 3
    5 4
    5 5
    """
    def __init__(self, lst):
        "*** YOUR CODE HERE ***"

    def __next__(self):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        "*** YOUR CODE HERE ***"

## Streams
def cycle(list):
    """
    Returns a Stream that cycles through each entry of the list.
    >>> s = cycle(['a', 'b', 'c'])
    >>> s.first
    'a'
    >>> s.rest.first
    'b'
    >>> s.rest.rest.rest.rest.first
    'b'
    >>> t = cycle([])
    >>> t is Stream.empty
    True
    >>> isinstance(s, Stream)
    True
    >>> isinstance(s.rest.rest, Stream)
    True
    """
    "*** YOUR CODE HERE ***"

def rle(s, max_run_length=10):
    """
    >>> example_stream = lst_to_stream([1, 1, 1, 2, 3, 3])
    >>> encoded_example = rle(example_stream)
    >>> stream_to_list(encoded_example, 3)
    [(3, 1), (1, 2), (2, 3)]
    >>> shorter_encoded_example = rle(example_stream, 2)
    >>> stream_to_list(shorter_encoded_example, 4)
    [(2, 1), (1, 1), (1, 2), (2, 3)]
    >>> ints = Stream(1, lambda: increment_stream(ints))
    >>> encoded_naturals = rle(ints)
    >>> stream_to_list(encoded_naturals, 3)
    [(1, 1), (1, 2), (1, 3)]
    >>> ones = Stream(1, lambda: ones)
    >>> encoded_ones = rle(ones, max_run_length=3)
    >>> stream_to_list(encoded_ones, 3)
    [(3, 1), (3, 1), (3, 1)]
    """
    "*** YOUR CODE HERE ***"
