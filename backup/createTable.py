import sqlite3

def create_blocks_table():
    conn = sqlite3.connect('blockchain.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Blocks (
            hash VARCHAR(66) PRIMARY KEY,
            parentHash VARCHAR(66),
            number INT,
            timestamp INT,
            nonce VARCHAR(18),
            difficulty INT,
            gasLimit VARCHAR(66),
            gasUsed VARCHAR(66),
            miner VARCHAR(42),
            extraData VARCHAR(66),
            baseFeePerGas VARCHAR(4)
        )
    ''')

    conn.commit()
    conn.close()

def create_block_transactions_table():
    conn = sqlite3.connect('blockchain.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS BlockTransactions (
            blockHash VARCHAR(66),
            transactionHash VARCHAR(66),
            PRIMARY KEY (blockHash, transactionHash),
            FOREIGN KEY (blockHash) REFERENCES Blocks(hash),
            FOREIGN KEY (transactionHash) REFERENCES Transactions(hash)
        )
    ''')

    conn.commit()
    conn.close()

def create_transactions_table():
    conn = sqlite3.connect('chainQ.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Transactions (
            hash VARCHAR(66) PRIMARY KEY,
            blockHash VARCHAR(66),
            type INT,
            accessList JSON,
            blockNumber INT,
            transactionIndex INT,
            confirmations INT,
            "from" VARCHAR(42),
            gasPrice JSON,
            maxPriorityFeePerGas JSON,
            maxFeePerGas JSON,
            gasLimit JSON,
            "to" VARCHAR(42),
            value JSON,
            nonce INT,
            data TEXT,            
            r VARCHAR(66),
            s VARCHAR(66),
            v INT,
            creates VARCHAR(42),
            chainId INT,
            FOREIGN KEY (blockHash) REFERENCES Blocks(hash)
        )
    ''')

    conn.commit()
    conn.close()

def create_all_tables():
    create_blocks_table()
    create_transactions_table()
    create_block_transactions_table()

if __name__ == "__main__":
    create_all_tables()
