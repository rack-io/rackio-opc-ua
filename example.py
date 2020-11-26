from rackio import Rackio, TagEngine
from rackio.controls import ValueAction, Condition, Control

from rackio_opcua import RackioOPCUA


app = Rackio()

tag_egine = TagEngine()

# Tags definitions

tag_egine.set_tag("T1", "float")
tag_egine.set_tag("T2", "float")
tag_egine.set_tag("T3", "float")

# Conditions definitions

cond1 = Condition("T1",">=", "T2")
cond2 = Condition("T1","<", "T2")

# Actions definitions

act1 = ValueAction("T3", 40)
act2 = ValueAction("T3", 80)

# Controls Definitions

control1 = Control("C1", cond1, act1)
control2 = Control("C2", cond2, act2)

app.append_control(control1)
app.append_control(control2)

# OPC mapping

driver = RackioOPCUA(app, port="8032")

folder = driver.define_folder("default")

device = folder.define_device("main")

device.define_mapping("T1", "write")
device.define_mapping("T2", "write")
device.define_mapping("T3", "read")

@app.rackit_on(period=1)
def reader():

    T1 = tag_egine.read_tag("T1")
    T2 = tag_egine.read_tag("T2")
    T3 = tag_egine.read_tag("T3")
        
    print("")
    print("T1   : {}".format(T1))
    print("T2   : {}".format(T2))
    print("T3   : {}".format(T3))
        

if __name__ == "__main__":

    app.run()