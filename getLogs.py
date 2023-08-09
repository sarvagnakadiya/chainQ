import asyncio
from web3 import Web3
import json
import os
from dotenv import load_dotenv
load_dotenv()
rpcUrl = os.getenv("RPC_URL")


outputFilePath = "logs.json"

# Connect to the Ethereum node
provider = Web3(Web3.HTTPProvider(rpcUrl))

async def listen_to_blocks():
    try:
        # block_number = 17839015
        # block = provider.eth.get_block(block_number)

        # alltx = block["transactions"]

        # logs_data = []
        # for txn_hash in alltx:
        log = provider.eth.get_transaction_receipt("0x3b6eb48536d917782ec3ac571e699546445e3c9072ae94e3747ed82a2d3f2398")
        print("logs are===============================================================================")
        print(log)
        # processed_log = {
        #     'transactionHash': log['transactionHash'].hex(),
        #     "address": log['address'] if 'address' in log else None,
        #     'blockHash': log['blockHash'].hex(),
        #     'blockNumber': log['blockNumber'],
        #     "data": log['data'] if 'data' in log else None,
        #     "logIndex": log['logIndex'] if 'logIndex' in log else None,
        #     "removed": log['removed'] if 'removed' in log else None,
        #     'topics': [topic.hex() for topic in log['topics']] if 'topics' in log else None,
        #     'values': log[]
        #     'transactionIndex': log['transactionIndex']
        # }
        # logs_data.append(processed_log)
        print("===============================================================================")

        # existingData = []
        # if os.path.exists(outputFilePath) and os.path.getsize(outputFilePath) > 0:
        #     with open(outputFilePath, "r") as file:
        #         existingData = json.load(file)

        # existingData.append(logs_data)

        # with open(outputFilePath, "w") as file:
        #     json.dump(existingData, file, indent=2)

    except Exception as e:
        print("Error:", e)

async def main():
    await listen_to_blocks()

if __name__ == "__main__":
    asyncio.run(main())
