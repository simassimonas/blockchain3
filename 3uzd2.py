from bitcoin.rpc import RawProxy
import sys, getopt
import hashlib

# converts big-endian values to little-endian
def bigToLittle(param):
    ba = bytearray.fromhex(param)
    ba.reverse()
    s = ''.join(format(x, '02x') for x in ba)
    return s
    

# Create a connection to local Bitcoin Core node
p = RawProxy()

# Get the block info 
blockheight = int(sys.argv[1])
blockhash = p.getblockhash(blockheight)
block = p.getblock(blockhash)

header_hex = (bigToLittle(block['versionHex']) + bigToLittle(block['previousblockhash']) 
+ bigToLittle(block['merkleroot']) + bigToLittle('{:02x}'.format(block['time'])) + bigToLittle(block['bits']) +  bigToLittle('{:02x}'.format(block['nonce'])) )

header_bin = header_hex.decode('hex')

hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()

if hash[::-1].encode('hex_codec')==block['hash']:
    print("Blocko hashas teisingas")
else:
    print("Blocko hashas neteisingas")

print(hash[::-1].encode('hex_codec'))
print(block['hash'])
