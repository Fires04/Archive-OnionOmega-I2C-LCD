import smbus
from time import *
from OmegaExpansion import onionI2C

class i2c_device:
   def __init__(self, addr, port=0):
      self.addr = addr
      self.i2c = onionI2C.OnionI2C(port)

# Write a single command
   def write_cmd(self, cmd):
      self.i2c.write(self.addr, cmd)
      sleep(0.0001)

# Write a command and argument
   def write_cmd_arg(self, cmd, data):
      self.i2c.writeByte(self.addr, cmd, data)
      sleep(0.0001)

# Write a block of data
   def write_block_data(self, cmd, data):
      self.i2c.writeBytes(self.addr, cmd, data)
      sleep(0.0001)

# Read a single byte
#   def read(self):
#      return self.bus.read_byte(self.addr)
#
## Read
#   def read_data(self, cmd):
#      return self.i2c.readBytes(self.addr, cmd,1)
#
## Read a block of data
#   def read_block_data(self, cmd):
#      return self.i2c.readBytes(self.addr, cmd)