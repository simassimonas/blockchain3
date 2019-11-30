from bitcoin.rpc import RawProxy
import sys, getopt

# Create a connection to local Bitcoin Core node
p = RawProxy()

# Retrieve the raw transaction by ID
txid = sys.argv[1]
raw_tx = p.getrawtransaction(txid)

# Decode the transaction
decoded_tx = p.decoderawtransaction(raw_tx)

# suranda output'o value
outputSum = 0
for output in decoded_tx['vout']:
    # Add up the value of each output
    outputSum += output['value']


# suranda input'u value
inputSum = 0
for input in decoded_tx['vin']:
    rawInputTransaction = p.getrawtransaction(input['txid'])
    InputTransaction = p.decoderawtransaction(rawInputTransaction)
    index = input['vout']   # rodo kelintas vout'as praeitam output'e
    tempVout = InputTransaction['vout']
    specificVout = tempVout[index]
    inputSum += specificVout['value']


print("Transakcijos mokestis: {} BTC".format(inputSum - outputSum))

