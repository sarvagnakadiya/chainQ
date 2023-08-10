import asyncio
from web3 import Web3
import json
import os
from dotenv import load_dotenv
load_dotenv()

rpcUrl = os.getenv("RPC_URL")
outputFilePath = "blocks.json"

# Connect to the Ethereum node
provider = Web3(Web3.HTTPProvider(rpcUrl))


def classify_transaction(input_data, to_address, value):
    # Check if the 'to' field is None or an Ethereum address (transfer)
    if to_address is None or to_address == "0x":
        if int(value, 16) > 0:  # Non-zero value indicates Ether transfer
            return "Ether Transfer"
        else:
            return "Unknown"  # No value indicates unknown transaction type

    # Convert input_data to bytes
    input_bytes = bytes.fromhex(input_data[2:])  # Remove the '0x' prefix

    # Check if the input data is non-empty (contract interaction)
    if input_bytes:
        # Token Transfers (ERC-20, ERC-721, ERC-1155)
        if input_bytes[:4] == b'\xa9\x05\x9c\xbb':  # ERC-20 transfer function selector
            return "ERC20 Transfer"
        elif input_bytes[:4] == b'\x23\xb8\x72\xdd':  # ERC-721 transfer function selector
            return "ERC721 Transfer"
        elif input_bytes[:4] == b'\xd9\xb6\xef\xce':  # ERC-1155 safeTransferFrom function selector
            return "ERC1155 Transfer"
        
        # Contract Deployment
        if to_address == "0x":
            return "Contract Deployment"
        
        # Token Approvals (ERC-20)
        if input_bytes[:10] == b'\x09\x5e\xa7\xb3':
            return "Token Approval"
        
        # Token Minting/Burning (Example prefixes, adjust as needed)
        if input_bytes[:4] == b'\x12\x34\x56\x78':
            return "Token Minting"
        if input_bytes[:4] == b'\x87\x65\x43\x21':
            return "Token Burning"
        
        # Contract Self-Destruction
        if input_bytes[:4] == b'\x30\xab\x71\x00':
            return "Contract Self-Destruction"

        # Other Contract Interactions
        return "Contract Interaction"
    
    return "Unknown"  # Default for unknown cases


async def get_latest_block_number():
    try:
        latest_block = provider.eth.get_block("latest")
        print(latest_block["number"])
        return latest_block["number"]
    except Exception as e:
        print("Error getting latest block number:", e)
        return None

async def listen_to_blocks():

    try:
        block_number = 17839015
        # 13062716

        	# 37808231
        block = provider.eth.get_block(block_number)
        print(block)

        # log = provider.eth.get_transaction_receipt(block['transactions'][2])
        # print("logs are===============================================================================")
        # print(log)
        # processed_log = {
        #     'transactionHash': log['transactionHash'].hex(),
        #     "address": log['address'] if 'address' in log else None,
        #     'blockHash': log['blockHash'].hex(),
        #     'blockNumber': log['blockNumber'],
        #     "data": log['data'] if 'data' in log else None,
        #     "logIndex": log['logIndex'] if 'logIndex' in log else None,
        #     "removed": log['removed'] if 'removed' in log else None,
        #     'topics': [topic.hex() for topic in log['topics']] if 'topics' in log else None,
        #     'transactionIndex': log['transactionIndex']
        # }
        # print("===============================================================================")
        # print(processed_log)

        # print("=============================finished==================================================")
        
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
        
       


        # withdrawals_list = []
        # for withdrawal in block["withdrawals"]:
        #     withdrawal_data = {
        #         "address": withdrawal["address"],
        #         "amount": int(withdrawal["amount"]),
        #         "index": int(withdrawal["index"]),
        #         "validatorIndex": int(withdrawal["validatorIndex"]),
        #     }
        #     withdrawals_list.append(withdrawal_data)

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
            "extraData": block["extraData"].hex(),
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

    except Exception as e:
        print("Error:", e)

async def main():
    # await listen_to_blocks()
    await get_latest_block_number()

if __name__ == "__main__":
    asyncio.run(main())
