## pyl 

pyl combines Pandoc Markdown with Python code execution:

    # Markdown header

    Here is some Python code

        x = 2 * 3 + 4
        z = 'A fine string'

    Now, is `x` = 10? and `z` a fine string?


### Usage

First install the scripts with

    $ python setup.py install

Then use either the build script

    $ pyl-build examples/basic.md > basic.html

or integrate the filter into your Pandoc chain

    $ pandoc --filter pyl-filter basic.md
