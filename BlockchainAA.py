import hashlib
import json
import time


class Block:
    def __init__(self, block_number, customer, location, flight, tag_number, bag_weight, nonce=0,
                 prev_hash=" ", timestamp=None):  # Initialize variables
        self.block_number = block_number
        self.customer = customer
        self.timestamp = timestamp or time.time()
        self.nonce = nonce
        self.prev_hash = prev_hash
        self.tag_number = tag_number
        self.bag_weight = bag_weight
        self.flight_number = flight
        self.location = location
        self.hash = self.calculate_hash()

    def calculate_hash(self):  # Will create the Digital Fingerprint or the Hash for the block
        block_str = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_str.encode()).hexdigest()

    def print_hashes(self):  # it prints the previous hash and the hash of the current block
        print("previous hash: " + self.prev_hash)
        print("hash: " + self.hash)


class Blockchain:
    chain = []

    def __int__(self):
        self.chain = []
        self.prev_hash = self.get_last_block()

    def genesis_block(self):  # Creates the first block in the blockchain
        genesis_block = Block(0, ["First Block"], time.time(), "0", "", "", "", "", "")
        genesis_block = genesis_block.calculate_hash()
        self.chain.append(genesis_block)
        return genesis_block

    def get_last_block(self):
        return self.chain[-1]  # This will return the last block in the Blockchain

    def add(self, block):  # This function adds a new block to the Blockchain
        self.prev_hash = self.get_last_block()
        self.block = block.calculate_hash()
        if self.verify(block) == False:
            return "Invalid Block... cannot verify block"
        elif self.verify(block) == True:
            return self.mine(block)

    def mine(self, block):  # this will mined the block that meets the requirement of the difficulty
        difficulty = 3  # the higher the number of the difficulty the longer it will take for the block to be mined.
        block.nonce = 0  # this is the number that is changed in order to obtain the hash that meets the requirement
        self.hash = block.calculate_hash()
        while not self.hash.startswith(
                '0' * difficulty):  # The number inside the parenthesis tells which number it must begin with
            block.nonce += 1
            # print(self.hash)
            self.hash = block.calculate_hash()
        self.chain.append(self.hash)
        return "---------------------------------------------" + \
               "\nMined Blocked :" + self.hash + \
               "\nNonce: " + str(block.nonce) + \
               "\nBlock Number: " + str(block.block_number) + \
               "\nCustomer: " + str(block.customer) + \
               "\nTag Number: " + str(block.tag_number) + \
               "\nFlight Number: " + str(block.flight_number) + \
               "\nBag Weight: " + str(block.bag_weight) + \
               "\nLocation: " + str(block.location) + \
               "\nTime: " + str(time.ctime(block.timestamp)) + \
               "\nPrevious Hash: " + str(self.prev_hash)

    def length_chain(self):
        return ("The length of the chain is: " + str(len(self.chain)))

    def index_chain(self):
        l = 0
        while len(self.chain) != l:
            for i in self.chain:
                print("\n Block " + str(l) + ": " + i)
                l += 1
            return ""

    def verify(self, block):  # verifies each block, aids in "consesus" process
        flag = True
        return flag


blocks = Blockchain()
print("Genesis Block: " + blocks.genesis_block())

num = int(input("Please Enter How many bags you are checking in/out"))
i = int(1)
while num >= i:
    customer = input("Please Enter the customer name: ")
    location = input("Please Enter the location from which you are checking in/out: ")
    flight = input("Please Enter the flight number")
    tag_number = input("Please Enter the tag number ")
    bag_weight = input("Please Enter the bag weight")
    print(blocks.add(Block(i, [customer], location, flight, tag_number, bag_weight)))
    i = i + 1
print("\n")
print("Last Block: " + blocks.get_last_block())
print("\n")

print(blocks.length_chain())
print(blocks.index_chain())
