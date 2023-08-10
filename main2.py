import asyncio
from web3 import Web3
import sqlite3
from dotenv import load_dotenv
import os
load_dotenv()

rpcUrl = os.getenv("RPC_URL")

# Connect to the Ethereum node
provider = Web3(Web3.HTTPProvider(rpcUrl))

# Create tables for `transaction_data`, `withdrawal_data`, and `block_data`
conn = sqlite3.connect("chainQ.db")
cursor = conn.cursor()
print("db created")

# Create a table for `transaction_data`
cursor.execute("""
CREATE TABLE IF NOT EXISTS transaction_data (
    blockHash TEXT,
    blockNumber INTEGER,
    chainId INTEGER,
    fromAddress TEXT,
    gas INTEGER,
    gasPrice INTEGER,
    hash TEXT,
    input TEXT,
    maxFeePerGas INTEGER,
    maxPriorityFeePerGas INTEGER,
    nonce INTEGER,
    r TEXT,
    s TEXT,
    toAddress TEXT,
    transactionIndex INTEGER,
    type TEXT,
    v INTEGER,
    value TEXT
)
""")

# Create a table for `withdrawal_data`
cursor.execute("""
CREATE TABLE IF NOT EXISTS withdrawal_data (
    address TEXT,
    amount INTEGER,
    withdrawal_index TEXT,
    validatorIndex INTEGER
)
""")

# Create a table for `block_data`
cursor.execute("""
CREATE TABLE IF NOT EXISTS block_data (
    blockHash TEXT PRIMARY KEY,
    parentHash TEXT,
    blockHeight INTEGER,
    timeStamp INTEGER,
    baseFeePerGas INTEGER,
    difficulty TEXT,
    logsBloom TEXT,
    miner TEXT,
    mixHash TEXT,
    nonce TEXT,
    receiptsRoot TEXT,
    sha3Uncles TEXT,
    size INTEGER,
    stateRoot TEXT,
    totalDifficulty TEXT,
    transactionsRoot TEXT,
    uncles TEXT,
    withdrawalsRoot TEXT,
    gasLimit TEXT,
    gasUsed INTEGER,
    extraData TEXT
)
""")

conn.commit()
conn.close()
print("tables created")

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
                "fromAddress": txn_data["from"],
                "gas": txn_data['gas'],
                "gasPrice": txn_data['gasPrice'],
                "hash": txn_data['hash'].hex(),
                "input": txn_data['input'].hex(),
                "maxFeePerGas": txn_data.get('maxFeePerGas'),
                "maxPriorityFeePerGas": txn_data.get('maxPriorityFeePerGas'),
                "nonce": txn_data['nonce'],
                "r": txn_data['r'].hex(),
                "s": txn_data['s'].hex(),
                "toAddress": txn_data['to'],
                "transactionIndex": txn_data['transactionIndex'],
                "type": txn_data['type'],
                "v": txn_data['v'],
                "value": str(txn_data['value']),  # Convert to string to handle large values
            }
            # print(transaction_data)
            # print("block data is loading...")
            txDetails.append(transaction_data)

        withdrawals_list = []
        for withdrawal in block["withdrawals"]:
            withdrawal_data = {
                "address": withdrawal["address"],
                "amount": int(withdrawal["amount"]),
                "withdrawal_index": str(withdrawal["index"]),  # Convert to string to store in SQLite
                "validatorIndex": int(withdrawal["validatorIndex"]),
            }
            withdrawals_list.append(withdrawal_data)

        block_data = {
            "blockHash": block["hash"].hex(),
            "parentHash": block["parentHash"].hex(),
            "blockHeight": block["number"],
            "timeStamp": block["timestamp"],
            "baseFeePerGas": block['baseFeePerGas'],
            "difficulty": int(block['difficulty']),  # Convert to integer to handle large values
            "logsBloom": block['logsBloom'].hex(),
            "miner": block["miner"],
            "mixHash": block['mixHash'].hex(),
            "nonce": block['nonce'].hex(),
            "receiptsRoot": block['receiptsRoot'].hex(),
            "sha3Uncles": block['sha3Uncles'].hex(),
            "size": block['size'],
            "stateRoot": block['stateRoot'].hex(),
            "totalDifficulty": int(block['totalDifficulty']),  # Convert to integer to handle large values
            "transactionsRoot": block['transactionsRoot'].hex(),
            "uncles": ",".join(block['uncles']),  # Flatten the list into a comma-separated string
            "withdrawals": withdrawals_list,
            "withdrawalsRoot": block['withdrawalsRoot'].hex(),
            "gasLimit": int(block["gasLimit"]),
            "gasUsed": int(block["gasUsed"]),
            "extraData": block["extraData"].hex(),
            "txDetails": txDetails,
        }

        conn = sqlite3.connect("chainQ.db")
        cursor = conn.cursor()

        # Insert data into the `transaction_data` table
        for txn in txDetails:
            cursor.execute("""
            INSERT INTO transaction_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                txn["blockHash"],
                txn["blockNumber"],
                txn["chainId"],
                txn["fromAddress"],
                txn["gas"],
                txn["gasPrice"],
                txn["hash"],
                txn["input"],
                txn["maxFeePerGas"],
                txn["maxPriorityFeePerGas"],
                txn["nonce"],
                txn["r"],
                txn["s"],
                txn["toAddress"],
                txn["transactionIndex"],
                txn["type"],
                txn["v"],
                txn["value"],
            ))
            
            
        # Insert data into the `withdrawal_data` table
        for withdrawal in withdrawals_list:
            cursor.execute("""
            INSERT INTO withdrawal_data VALUES (?, ?, ?, ?)
            """, (
                withdrawal["address"],
                withdrawal["amount"],
                withdrawal["withdrawal_index"],
                withdrawal["validatorIndex"],
            ))


        # Convert large integer values to strings before inserting into the database
        block_data["difficulty"] = str(block_data["difficulty"])
        block_data["totalDifficulty"] = str(block_data["totalDifficulty"])
        block_data["gasLimit"] = str(block_data["gasLimit"])
        # Insert data into the `block_data` table
        cursor.execute("""
        INSERT INTO block_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            block_data["blockHash"],
            block_data["parentHash"],
            block_data["blockHeight"],
            block_data["timeStamp"],
            block_data["baseFeePerGas"],
            block_data["difficulty"],
            block_data["logsBloom"],
            block_data["miner"],
            block_data["mixHash"],
            block_data["nonce"],
            block_data["receiptsRoot"],
            block_data["sha3Uncles"],
            block_data["size"],
            block_data["stateRoot"],
            block_data["totalDifficulty"],
            block_data["transactionsRoot"],
            block_data["uncles"],
            block_data["withdrawalsRoot"],
            block_data["gasLimit"],
            block_data["gasUsed"],
            block_data["extraData"],
        ))

        conn.commit()
        conn.close()
        print("values inserted")
    except Exception as e:
        print("Error:", e)

async def main():
    await listen_to_blocks()

if __name__ == "__main__":
    asyncio.run(main())
