import sys
from bitcoin.rpc import RawProxy
p = RawProxy()
txhash = sys.argv[1]
raw_tx = p.getrawtransaction(txhash)
decoded_tx = p.decoderawtransaction(raw_tx)
total = 0
transactionvalue = 0
for item in decoded_tx['vin']:
        vout = item['vout']
        txid = item['txid']
        raw_txN = p.getrawtransaction(txid)
        decoded_txN = p.decoderawtransaction(raw_txN)
        for output in decoded_txN['vout']:
                if(output['n'] == vout):
                        total = total + output['value']
for output in decoded_tx['vout']:
        transactionvalue = transactionvalue + output['value']
transactionfee = total - transactionvalue
print transactionfee