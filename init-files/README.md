LagoInitFile examples
---------------------
This directory contains of LagoInitFiles examples, each example can be used
by running:

```bash
  $ lago init <filename>
```

Or from Python:

```python

from lago import sdk

env = sdk.init(config='<filename>',
               workdir='/tmp/lago-workdir')
```
