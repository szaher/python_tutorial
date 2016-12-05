Generators
==========

> One of the most powerfull applications of generators is setting up processing
  pipelines.
> Similar to shell pipes in Unix

input => Generator => Generator => Generator > for x in a: do ...

> The idea is to stack a series of generator functions together into a pipe
  and pull items through it with a for loop