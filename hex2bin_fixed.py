#!/usr/bin/env python3

# Parser for Intel HEX format, intentionally lenient

# This can parse .hex files from the Nintendo leaks, since they use a variant of the format
# with a 3-byte payload in the extended segment address records (most other tools reject this).

# Usage: ./hex2bin_fixed.py input.hex > out.bin
# (ie. hex file from stdin (or filename arg), data to stdout)
# If you're using PowerShell... don't; it seems to re-encode the data into UTF-16, breaking it. >.>

import binascii, fileinput, os, sys

def checksum_of(data):
    # Sum of byte values
    chk = 0
    for b in data:
        chk = (chk + b) & 0xff

    # Checksum is two's complement of sum
    return (~chk + 1) & 0xff

def parse_record(lineno, line):
    if not line.startswith(":"):
        return None

    bs = binascii.unhexlify(line[1:])

    count = bs[0]
    addr = bs[1] << 8 | bs[2]
    rtype = bs[3]
    payload = bs[4:-1]
    checksum = bs[-1]

    if len(payload) != count:
        print("error: invalid payload length on line {} (expected {:02X} bytes, got {:02X})".format(lineno, count, len(payload)), file=sys.stderr)
    
    actual_checksum = checksum_of(bs[:-1])
    if actual_checksum != checksum:
        print("error: invalid checksum on line {} (expected {:02X}, got {:02X})".format(lineno, checksum, actual_checksum), file=sys.stderr)
        sys.exit(1)

    return (rtype, addr, payload)

data = bytearray()
offset = 0

for (lineno, line) in enumerate(fileinput.input()):
    
    # Skip lines that don't start with a :
    if not line.startswith(":"):
        continue

    rtype, addr, payload = parse_record(lineno, line.strip())
    if rtype == 0:
        # Data literal, just write to buffer
        start_addr = offset + addr
        end_addr = offset + addr + len(payload)
        
        # Extend byte array so the data fits
        if len(data) < end_addr:
            new_size = end_addr - len(data)
            data.extend(bytearray(new_size))
        
        # Fill array
        data[start_addr:end_addr] = payload
    elif rtype == 1:
        # End of file
        break
    elif rtype == 2:
        # Extended segment address, set offset for future data
        # NOTE: File format specifies this must be 2 bytes,
        # but Nintendo seems to use a format with 3 bytes... >.>
        offset = int.from_bytes(payload, byteorder="big", signed=False) * 16
    else:
        # We don't support Start Segment Address (03), 
        # Extended Linear Address (04) or Start Linear Address (05)
        # those seem to be x86-specific anyway, so meh
        print("error: unsupported record type {:02X}".format(rtype), file=sys.stderr)
        sys.exit(1)
else:
    # We ran out of lines before hitting an end of file record (which would break)
    print("error: hit end of input before EOF record", file=sys.stderr)
    sys.exit(1)

# Print output data to stdout
#sys.stdout.buffer.write(bytes(data))
#sys.stdout.buffer.flush()
with open(fileinput.filename() + ".bin", "wb") as file:
    file.write(bytes(data))
# :)
sys.exit(0)
