import asyncio
from web3 import Web3
from dotenv import load_dotenv
import os
import json
load_dotenv()

rpcUrl = os.getenv("RPC_URL")

# Connect to the Ethereum node
provider = Web3(Web3.HTTPProvider("https://opt-mainnet.g.alchemy.com/v2/cfV5n_qtluCSUthXagbF9heGZBi_PZKW"))

limit = 108002722
async def get_latest_block_number():
    try:
        latest_block = provider.eth.get_block("latest")
       
        return latest_block["number"]
    except Exception as e:
        print("Error getting latest block number:", e)
        return None
    



outputFilePath = "blocks.json"

async def listen_to_blocks():
    try:
        block_num = 108019738
        latestBlock = await get_latest_block_number()
        # ekVar = True
        while True:
            try:
                block = provider.eth.get_block(block_num)
                if block is None:
                    continue

                alltx = block["transactions"]

                txDetails = []
                for txn_hash in alltx:
                    txn_data = provider.eth.get_transaction(txn_hash)
                    print(txn_data)
                    print("=-=-=---=-=-=-=-=-=-=-=-=-=-=-=-=-")
                    # log_data = provider.eth.get_transaction_receipt(txn_data)
                    transaction_data = {
                        "transactionHash": txn_hash.hex(),
                        "blockHash": txn_data["blockHash"].hex(),
                        "blockNumber": txn_data["blockNumber"],
                        # "chainId": txn_data['chainId'],
                        "chainId": txn_data['chainId'] if 'chainId' in txn_data else None,
                        "from": txn_data["from"],
                        "gas": txn_data['gas'],
                        "gasPrice": txn_data['gasPrice'],
                        "hash": txn_data['hash'].hex(),
                        "input": txn_data['input'].hex(),
                        "maxFeePerGas": txn_data['maxFeePerGas'] if 'maxFeePerGas' in txn_data else None,
                        "maxPriorityFeePerGas": txn_data['maxPriorityFeePerGas'] if 'maxPriorityFeePerGas' in txn_data else None,
                        "nonce": txn_data['nonce'],
                        "r": txn_data['r'].hex(),
                        "s": txn_data['s'].hex(),
                        "to": txn_data['to'],
                        "transactionIndex": txn_data['transactionIndex'],
                        "type": txn_data['type'],
                        "v": txn_data['v'],
                        "value": txn_data["value"],
                        # "types": classify_transaction(txn_data['input'].hex(), txn_data['to'], txn_data['value'])
                    }
                    # print(transaction_data)
                    txDetails.append(transaction_data)
                
            
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
                    # "withdrawals": withdrawals_list,
                    # "withdrawalsRoot": block['withdrawalsRoot'].hex(),
                    "gasLimit": int(block["gasLimit"]),
                    "gasUsed": int(block["gasUsed"]),
                    # "extraData": block["extraData"].hex(),
                    "txDetails": txDetails,
                }

                print("---------------------------------------------------------------------------")
                # print(block_data)

                existingData = []
                if os.path.exists(outputFilePath) and os.path.getsize(outputFilePath) > 0:
                    with open(outputFilePath, "r") as file:
                        existingData = json.load(file)

                existingData.append(block_data)

                with open(outputFilePath, "w") as file:
                    json.dump(existingData, file, indent=2)

                block_num+=1
           
                if block_num > latestBlock:
                    await asyncio.sleep(2)  # Wait for 1 second before checking again
                    continue

            except Exception as e:
                print(f"Error processing block {block_num}:", e)

    except Exception as e:
        print("Error:", e)



async def main():
    await listen_to_blocks()

if __name__ == "__main__":
    asyncio.run(main())