# rackio-opc-ua
A Rackio extension to add a OPC-UA support to a Rackio application

## Installation

```
pip install RackioOPC-UA
```

## Usage

```python
from rackio import Rackio
from rackio_opcua import RackioOPCUA

app = Rackio()

RackioOPCUA(app, 4840)

app.run(8028)
```

