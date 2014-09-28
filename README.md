# TP-SG105(RTL8367) Modification

The RTL8367 switch controller in the TP-SG105 can modified by setting the registers through the EEPROM SMI interface. Quick way to do this is to connect with the SDA and SCL pin on the EEPROM (M24C08) using a buspirate.

The commands to do trivial tasks like forcing the LED to be on can be found in *TL-SG105/buspirate_cmd.txt*

The RTL8367 is configured on power-on by loading register settings from the EEPROM. The first 2 bytes in the EEPROM will define when to stop reading from the EEPROM.

> Example: 0xA6 0x81 -> 0x81A6 (read until 0x01A6)

The rest of the EEPROM are pairs of register (2 bytes) and value(2 bytes).

> Example: 0x05 0x13 0x00 0xC0 -> load 0xC000 to register 0x1305

Changes can be made by writing the register and value pair to load into EEPROM, then modify the first 2 bytes to read until pass the new register and value pair.

<img src="https://bytebucket.org/jiajun/rtl8xxx-switch/raw/c7d40a70a67ef0320366f2b322a71cd31f329323/TL-SG105/pcb.jpg" style="height:360">
