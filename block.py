import hashlib
import time

class Block:
    def __init__(self, index, proof_no, prev_hash, completed_transactions, timestamp=None):
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.completed_transactions = completed_transactions
        self.timestamp = timestamp or time.time()

    def calculate_hash(self):
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_no,
                                              self.prev_hash, self.transactions_completed,
                                              self.timestamp)

        return hashlib.sha256(block_of_string.encode()).hexdigest()

    def __repr__(self):
        return "index: {} \n proof_no: {} \n prev_hash: {} \n completed_transactions: {} \n timestamp: {}".format(self.index, self.proof_no,
                                               self.prev_hash, self.completed_transactions,
                                               self.timestamp)
