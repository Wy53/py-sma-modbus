from datetime import datetime

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder


class Value:
    def __init__(self, value):
        self.date = datetime.timestamp(datetime.now())
        self.value = value


class Register:
    def __init__(self, id, name, description, client, length):
        self.id = id
        self.name = name
        self.description = description
        self.length = length
        self.value = None
        self.registers = []
        self.client = client
        self.slave = 3

    def __str__(self):
        return f"{self.id} {self.name} ({self.description})"

    def set_registers(self, registers):
        self.registers = registers

    def is_null(self):
        return None

    def get_value(self):
        return None


class S16(Register):
    def __init__(self, register_id, name, description, client, length=1):
        Register.__init__(self, register_id, name, description, client, length)

    def get_value(self):
        result = self.client.read_input_registers(self.id,count=self.length, slave=self.slave)
        decode = self.client.convert_from_registers(result.registers, data_type=self.client.DATATYPE.INT16)
        return decode

    def is_null(self):
        return self.get_value() == 0x8000


class S32(Register):
    def __init__(self, register_id, name, description, client, length=2):
        Register.__init__(self, register_id, name, description, client, length)

    def get_value(self):
        result = self.client.read_input_registers(self.id,count=self.length, slave=self.slave)
        decode = self.client.convert_from_registers(result.registers, data_type=self.client.DATATYPE.INT32)
        return decode

    def is_null(self):
        return self.get_value() == 0x80000000


class U16(Register):
    def __init__(self, register_id, name, description, client, length=1):
        Register.__init__(self, register_id, name, description, client, length)

    def get_value(self):
        result = self.client.read_input_registers(self.id,count=self.length, slave=self.slave)
        decode = self.client.convert_from_registers(result.registers, data_type=self.client.DATATYPE.UINT16)
        return decode

    def is_null(self):
        return self.get_value() == 0xFFFF


class U32(Register):
    def __init__(self, register_id, name, description, client, length=2):
        Register.__init__(self, register_id, name, description, client, length)

    def get_value(self):
        result = self.client.read_input_registers(self.id,count=self.length, slave=self.slave)
        decode = self.client.convert_from_registers(result.registers, data_type=self.client.DATATYPE.UINT32)
        return decode

    def is_null(self):
        return self.get_value() == 0xFFFFFFFF or self.get_value() == 0xFFFFFD


class U64(Register):
    def __init__(self, register_id, name, description, client, length=4):
        Register.__init__(self, register_id, name, description, client, length)

    def get_value(self):
        result = self.client.read_input_registers(self.id,count=self.length, slave=self.slave)
        decode = self.client.convert_from_registers(result.registers, data_type=self.client.DATATYPE.UINT64)
        return decode

    def is_null(self):
        return self.get_value() == 0xFFFFFFFFFFFFFFFF


class STR32(Register):
    def __init__(self, register_id, name, description,client , length=8):
        Register.__init__(self, register_id, name, description,client , length)

    def get_value(self):
        result = self.client.read_input_registers(self.id,count=self.length, slave=self.slave)
        decode = self.client.convert_from_registers(result.registers, data_type=self.client.DATATYPE.STR32)
        return decode

    def is_null(self):
        return self.get_value() == ""
