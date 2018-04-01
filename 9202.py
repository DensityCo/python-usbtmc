import usbtmc
print ("a")
instr =  usbtmc.Instrument(0xffff, 0x9200)
#instr =  usbtmc.Instrument("USB::0xFFFF::0x9202::INSTR")
print ("b")
print(instr.ask("*IDN?"))
    # returns 'AGILENT TECHNOLOGIES,MSO7104A,MY********,06.16.0001'

