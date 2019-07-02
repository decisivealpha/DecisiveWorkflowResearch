README
======

- Python 3.6

Setup
-----

1. Strip your notebooks with nbstripout before commiting to remove the output
  - To easily strip your notebook outputs, 'pip install nbstripout' and add this to your .git/config:
        [filter "nbstripout"]
            clean = "/path/to/nbconvert/nbstripout"
  - Alternatively, you can run 'nbstripout <notebook>'

