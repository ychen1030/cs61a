class Stream:
    empty = 'empty'
    def __init__(self, first, compute_rest=lambda: Stream.empty):
        self.first = first
        self.cached_rest = None
        assert callable(compute_rest)
        self.compute_rest = compute_rest
    @property
    def rest(self):
        """Return the rest, computing it if necessary."""
        if self.compute_rest is not None:
            self.cached_rest = self.compute_rest()
            self.compute_rest = None
        return self.cached_rest
    def __repr__(self):
        rest = self.cached_rest if self.compute_rest is None else '<...>'
        return 'Stream({}, {})'.format(self.first, rest)
def lst_to_stream(lst):
    if not lst:
        return Stream.empty
    return Stream(lst[0], lambda: lst_to_stream(lst[1:]))
def stream_to_list(s, n=10):
    """A list containing the elements of stream S,
    up to a maximum of N."""
    r = []
    while n > 0 and s is not Stream.empty:
        r.append(s.first)
        s = s.rest
        n -= 1
    return r
def increment_stream(s):
    """Increment all elements of a stream."""
    return Stream(s.first+1, lambda: increment_stream(s.rest))

# The stream of consecutive integers starting at 1.
ints = Stream(1, lambda: increment_stream(ints))