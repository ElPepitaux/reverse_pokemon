import sys

if __name__ == "__main__":
    with open(sys.argv[1], "rb+") as f:
        sav = bytearray(f.read()) # This variable is an array containing each bytes of your save file. If you want to modify the byte at address 0x42DE to the value 0x83 for example you can simply use sav[0x42DE] = 0x83 (just like a normal array :-))
        # Write some code here


        checksum = 0xff
        # sav[0x2598] = 0x85
        # sav[0x2599] = 0x93
        # sav[0x259A] = 0x88
        # sav[0x259B] = 0x81
        # sav[0x259C] = 0x83
        # sav[0x259D] = 0x8E
        # sav[0x259E] = 0x91

        # sav[0x25CB] = 0x05

        # sav[0x25CE] = 0x01
        # sav[0x25CF] = 0x63
        # sav[0x25D0] = 0xFF

        sav[0x2F2D] = 0x83
        sav[0x2F34] = 0x83

        sav[0x2F35] = 0x01
        sav[0x2F36] = 0x5E
        sav[0x2F37] = 0x64
        sav[0x2F55] = 0x64
        sav[0x2F58] = 0x07
        sav[0x2F59] = 0xD0

        sav[0x2F5A] = 0x07
        sav[0x2F5B] = 0xD0

        sav[0x2F5C] = 0x07
        sav[0x2F5D] = 0xD0

        sav[0x2F5E] = 0x07
        sav[0x2F5F] = 0xD0

        sav[0x3523] = checksum & 0xff
        f.seek(0, 0)
        f.write(sav)
