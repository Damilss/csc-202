# Correction notes (tsort)

## My first draft 
commit `c3e38f1d8fabe65812a8812e92dcf6dccef5e466` 

- Mixing outgoing degree logic with in-degree logic

- looping over a list while mutating it, causing certain elements to be missed and jumped over elements (common bug)

- Some simpler ways to write certain arguments/elements

- wrong cycle check with wrong logic. Had to reearch how to properly find cycles 

- Completely forgot about the usage of sets 
    - used for finding all of the inital 0 in-degree verticies

**Extra concepts learned**: 
- learned different characteristics for defaultdict()

- **core concept**, mutating a loop while iterating is a very common mistake 

### Corrected draft
commit `14365175f9087c8a9a5f7fa058ca6ecb44826f4a`