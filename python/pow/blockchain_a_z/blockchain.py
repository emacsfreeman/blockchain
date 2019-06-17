################
## Importations
###############

import datetime
# https://docs.python.org/3/library/datetime.html

import hashlib
# https://docs.python.org/3/library/hashlib.html

import json
# https://docs.python.org/3/library/json.html

from flask import Flask, jsonify
# Flask: http://flask.pocoo.org/docs/1.0/latexindex/?highlight=flask

# jsonify: http://flask.pocoo.org/docs/1.0/api/?highlight=jsonify#flask.json.jsonify



class Blockchain:

  def __init__(self):
    self.chain = []
    self.create_block(proof = 1, previous_hash = '0')

  def create_block(self, proof, previous_hash):
    # définition du dico block
    block = 
    { 
      'index': len(self.chain) + 1, 
      'timestamp': str(datetime.datetime.now()),
      'proof': proof,
      'previous_hash': previous_hash
    }
    # ajout du bloc à la chaîne
    self.chain.append(block)
    
    return block

  def get_previous_block(self):
    return self.chain[-1]

  def proof_of_work(self, previous_proof):
    new_proof = 1
    check_proof = False
    while check_proof is False:
      hash_operation = hashlib.sha256(str(new_proof**2 + previous_proof**2).encode()).hexdigest()
      if hash_operation[:4] = '0000':
        check_proof = True
      else:
        new_proof += 1
    return new_proof

  def hash(self, block):
    encoded_block = json.dumps(block, sort_keys = True).encode()
    return hashlib.sha256(encoded_block).hexdigest()
  
  def is_chain_valid(self, chain):
    previous_block = chain[0]
    block_index = 1
    while block_index < len(chain):
      block = chain[block_index]
      if block['previous_hash'] != self.hash(previous_block):
        return False
      previous_proof = previous_block['proof']
      proof = block['proof']
      hash_operation = hashlib.sha256(str(proof**2 + previous_proof**2).encode()).hexdigest()
      if hash_operation[:4] != '0000':
        return False
      previous_block = block
      block += 1
    return True
