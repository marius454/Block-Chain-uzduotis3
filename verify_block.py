from binascii import unhexlify
from hashlib import sha256
import sys
from bitcoin.rpc import RawProxy


def littleEndian(string):
        splited = [str(string)[i:i + 2] for i in range(0, len(str(string)), 2)]
        splited.reverse()
        return "".join(splited)

p = RawProxy()
blockhash = sys.argv[1]
block = p.getblockheader(blockhash)

little_endian_version = littleEndian(block['versionHex'])
little_endian_previousHash = littleEndian(block['previousblockhash'])
little_endian_merkleRoot = littleEndian(block['merkleroot'])
little_endian_time = littleEndian(hex(block['time'])[2:])
little_endian_difficultyBits = littleEndian(block['bits'])
little_endian_nonce = littleEndian(hex(block['nonce'])[2:])

header = little_endian_version + little_endian_previousHash + little_endian_merkleRoot + little_endian_time + little_endian_difficultyBits + little_endian_nonce
header = unhexlify(header)

CalculatedHash = sha256(sha256(header).digest()).hexdigest()
result = littleEndian(CalculatedHash)

print "Original hash: ", blockhash
print "Calculated hash: ", result

if blockhash == result:
        print "Block hash is verified"
else:
        print "Block hash is not verified"