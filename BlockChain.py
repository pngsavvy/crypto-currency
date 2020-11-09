
class BlockChain:
    def __init__(self):
        pass

    def contruct_genesis(self):
        pass

    def construct_block(self):
        pass

    @staticmethod
    def check_validity():
        pass

    def new_data(self, sender, recipient, quantity):
        pass

    @staticmethod
    def contruct_proof_of_work(prev_proof):
        pass

    @property
    def last_block(self):
        return self.chain[-1]