import asyncio
from web3 import Web3
import json
import os

rpcUrl = "https://eth-mainnet.g.alchemy.com/v2/40NCT0StPsfEZkWeZu8-E4ByKln3pSCW"
outputFilePath = "blocks.json"

# Connect to the Ethereum node
provider = Web3(Web3.HTTPProvider(rpcUrl))


async def listen_to_blocks():
    try:
        block_number = 17839015
        block = provider.eth.get_block(block_number)
        # print(block)
        


        alltx = block["transactions"]

        txDetails = []
        for txn_hash in alltx:
            txn_data = provider.eth.get_transaction(txn_hash)
            transaction_data = {
                "blockHash": txn_data["blockHash"].hex(),
                "blockNumber": txn_data["blockNumber"],
                "chainId": txn_data['chainId'],
                "from": txn_data["from"],
                "gas": txn_data['gas'],
                "gasPrice": txn_data['gasPrice'],
                "hash": txn_data['hash'].hex(),
                "input": txn_data['input'].hex(),
                "maxFeePerGas": txn_data['maxFeePerGas'] if 'maxFeePerGas' in txn_data else None,
                "maxPriorityFeePerGas": txn_data['maxPriorityFeePerGas'] if 'maxPriorityFeePerGas' in txn_data else None,
                # "maxPriorityFeePerGas": txn_data['maxPriorityFeePerGas'],
                "nonce": txn_data['nonce'],
                "r": txn_data['r'].hex(),
                "s": txn_data['s'].hex(),
                "to": txn_data['to'],
                "transactionIndex": txn_data['transactionIndex'],
                "type": txn_data['type'],
                "v": txn_data['v'],
                "value": txn_data['value'], 
            }
            print(transaction_data)
            txDetails.append(transaction_data)
        
        # txDetails.append(dict(txn_data))  # Convert AttributeDict to regular dictionary


        withdrawals_list = []
        for withdrawal in block["withdrawals"]:
            withdrawal_data = {
                "address": withdrawal["address"],
                "amount": int(withdrawal["amount"]),
                "withdrawal_index": int(withdrawal["index"]),
                "validatorIndex": int(withdrawal["validatorIndex"]),
            }
            withdrawals_list.append(withdrawal_data)

        block_data = {
            "blockHash": block["hash"].hex(),
            "parentHash": block["parentHash"].hex(),
            "blockHeight": block["number"],
            "timeStamp": block["timestamp"],
            "baseFeePerGas": block['baseFeePerGas'],
            "difficulty": block['difficulty'],
            "logsBloom": block['logsBloom'].hex(),
            "miner": block["miner"],
            "mixHash": block['mixHash'].hex(),
            "nonce": block['nonce'].hex(),
            "receiptsRoot": block['receiptsRoot'].hex(),
            "sha3Uncles": block['sha3Uncles'].hex(),
            "size": block['size'],
            "stateRoot": block['stateRoot'].hex(),
            "totalDifficulty": block['totalDifficulty'],
            "transactionsRoot": block['transactionsRoot'].hex(),
            "uncles": block['uncles'],
            "withdrawals": withdrawals_list,
            "withdrawalsRoot": block['withdrawalsRoot'].hex(),
            "gasLimit": int(block["gasLimit"]),
            "gasUsed": int(block["gasUsed"]),
            "extraData": block["extraData"].hex(),
            "txDetails": txDetails,
        }

        print("---------------------------------------------------------------------------")
        print(block_data)

        existingData = []
        if os.path.exists(outputFilePath) and os.path.getsize(outputFilePath) > 0:
            with open(outputFilePath, "r") as file:
                existingData = json.load(file)

        existingData.append(block_data)

        with open(outputFilePath, "w") as file:
            json.dump(existingData, file, indent=2)

    except Exception as e:
        print("Error:", e)

async def main():
    await listen_to_blocks()

if __name__ == "__main__":
    asyncio.run(main())
