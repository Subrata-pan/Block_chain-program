import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_str = str(self.index) + str(self.timestamp) + self.data + self.previous_hash + str(self.nonce)
        return hashlib.sha256(block_str.encode()).hexdigest()

blockchain = []
genesis_block = Block(0, "Genesis Block", "0")
blockchain.append(genesis_block)

for i in range(1, 3):
    new_block = Block(i, f"Block {i} Data", blockchain[-1].hash)
    blockchain.append(new_block)

for block in blockchain:
    print(f"Block {block.index} | Hash: {block.hash} | Prev: {block.previous_hash}")

print("\nTampering Block 1...")
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].calculate_hash()


for block in blockchain:
    print(f"Block {block.index} | Hash: {block.hash} | Prev: {block.previous_hash}")
