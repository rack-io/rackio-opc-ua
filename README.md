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

driver = RackioOPCUA(app, 4840)

app.run(8028)
```

## Creating Tree Nodes

In order to create nodes, you can define custom folders, devices and mappings.

```python
folder = driver.define_folder("default")

device = folder.define_device("main")
```

Mappings allows to bind a OPC-UA object node to a Rackio defined Tag.

```python
device.define_mapping("T1", "write")
device.define_mapping("T3", "read")
```

*write* mode allows to read and write from a OPC-UA Client, and *read* mode allows to read only. By default, the binding timing period is *0.25* seconds. You bypass this by providing the *period* parameter, in seconds.

```python
device.define_mapping("T1", "read", period=0.5)
```

You can also define mappings inside folders and can define folders inside folders.

## Features to develop

Some OPC-UA features are in development phase suchas.

* Custom Method definitions
* Custom Data Types definitions
* History Query
* Loading configurations form a file (*JSON* and *XML*)
