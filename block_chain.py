from block import Block
import hashlib

class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_completed_transactions = []
        self.nodes = set()
        self.contruct_genesis()

    def contruct_genesis(self):
        self.construct_block(proof_no=0, prev_hash=0)

    def construct_block(self, proof_no, prev_hash):
        block = Block(
            index=len(self.chain),
            proof_no=proof_no,
            prev_hash=prev_hash,
            completed_transactions=self.current_completed_transactions
        )
        self.current_completed_transactions = []

        self.chain.append(block)
        return block

    @staticmethod
    def check_validity(block, prev_block):
        if prev_block.index + 1 != block.index:
            return False
        
        elif prev_block.calculate_hash != block.prev_hash:
            return False
        
        elif not BlockChain.verifying_proof(block.proof_no, prev_block.proof_no):
            return False
        
        elif block.timestamp <= prev_block.timestamp:
            return False
        
        return True
    


    def new_data(self, sender, recipient, quantity):
        self.current_completed_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'quantity': quantity
        })
        return True

    @staticmethod
    def proof_of_work(last_proof):
        proof_no = 0
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1
        return proof_no

    @staticmethod 
    def verifying_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @staticmethod
    def contruct_proof_of_work(prev_proof):
        pass

    @property
    def latest_block(self):
        return self.chain[-1]