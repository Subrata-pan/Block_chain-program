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

    def mine_block(self, difficulty):
        print(f"Mining block with difficulty {difficulty}...")
        start_time = time.time()
        target = '0' * difficulty
        attempts = 0

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1

        end_time = time.time()
        print(f"Block mined: {self.hash}")
        print(f"Nonce attempts: {attempts}")
        print(f"Time taken: {end_time - start_time:.2f}s\n")

# Mining example
block = Block(0, "Test Mining", "0")
block.mine_block(difficulty=4)
