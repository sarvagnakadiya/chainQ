import sqlite3
import json

# Load the existing data from the JSON file
with open("blocks.json", "r") as file:
    existingData = json.load(file)

# Connect to the SQLite database or create it if it doesn't exist
conn = sqlite3.connect("chainQ.db")
cursor = conn.cursor()

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
    withdrawal_index INTEGER,
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
    gasLimit INTEGER,
    gasUsed INTEGER,
    extraData TEXT
)
""")

# Insert data into the `transaction_data` table
for block in existingData:
    for txn in block["txDetails"]:
        cursor.execute("""
        INSERT INTO transaction_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            txn["blockHash"],
            txn["blockNumber"],
            txn["chainId"],
            txn["from"],
            txn["gas"],
            txn["gasPrice"],
            txn["hash"],
            txn["input"],
            txn["maxFeePerGas"],
            txn["maxPriorityFeePerGas"],
            txn["nonce"],
            txn["r"],
            txn["s"],
            txn["to"],
            txn["transactionIndex"],
            txn["type"],
            txn["v"],
            # txn["value"]
            str(txn["value"])
        ))

# Insert data into the `withdrawal_data` table
for block in existingData:
    for withdrawal in block["withdrawals"]:
        cursor.execute("""
        INSERT INTO withdrawal_data VALUES (?, ?, ?, ?)
        """, (
            withdrawal["address"],
            withdrawal["amount"],
            # withdrawal["withdrawal_index"],
            str(withdrawal["withdrawal_index"]),
            withdrawal["validatorIndex"]
        ))

# Insert data into the `block_data` table
for block in existingData:
    cursor.execute("""
    INSERT INTO block_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        block["blockHash"],
        block["parentHash"],
        block["blockHeight"],
        block["timeStamp"],
        block["baseFeePerGas"],
        block["difficulty"],
        block["logsBloom"],
        block["miner"],
        block["mixHash"],
        block["nonce"],
        block["receiptsRoot"],
        block["sha3Uncles"],
        block["size"],
        block["stateRoot"],
        block["totalDifficulty"],
        block["transactionsRoot"],
        block["uncles"],
        block["withdrawalsRoot"],
        block["gasLimit"],
        block["gasUsed"],
        block["extraData"]
    ))

# Commit the changes and close the connection
conn.commit()
conn.close()
