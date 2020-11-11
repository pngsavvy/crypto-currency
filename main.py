from block_chain import BlockChain

blockchain = BlockChain()

print("***Mining coolCoin about to start***")
print(blockchain.chain)

last_block = blockchain.latest_block
last_proof_no = last_block.proof_no
proof_no = blockchain.proof_of_work(last_proof_no)

running = True

while running:
    sender = input("sender: ")
    recipient = input("recipient: ")
    quantity = input("quantity: ")

    blockchain.new_data(
        sender=sender, 
        recipient=recipient, 
        quantity=quantity,
    )

    last_hash = last_block.calculate_hash
    block = blockchain.construct_block(proof_no, last_hash)

    print("***Mining fccCoin has been successful***")
    print(blockchain.chain)

    keepGoing = input("complete another transaction? (Y/N)").upper()
    
    if keepGoing == "Y":
        running = True
    else:
        running = False