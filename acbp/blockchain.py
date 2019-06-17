from functools import reduce
import hashlib as hl

import json
import pickle
import requests

# Importations
from utility.hash_util import hash_block
from utility.verification import Verification
from block import Block
from transaction import Transaction
from wallet import Wallet

# Récompense de minage
MINING_REWARD = 12.50

print(__name__)

class Blockchain:
    """
    La classe Blockchain gères la chaîne de blocs, les transactions
    ouvertes et le noeud sur lequel elles sont effectuées.

    Attributs:
        :chain: La liste de blocs
        :open_transactions (privée): La liste des transactions ouvertes
        :hosting_node: Le noeud connecté (qui lance la blockchain).
    """

    def __init__(self, public_key, node_id):
        """Le constructeur de la classe Blockchain."""
        # Notre bloc de départ de la blockchain
        genesis_block = Block(0, '', [], 100, 0)
        # Initialisation
        self.chain = [genesis_block]
        # Transactions non gérées
        self.__open_transactions = []
        self.public_key = public_key
        self.__peer_nodes = set()
        self.node_id = node_id
        self.resolve_conflicts = False
        self.load_data()



    # Cela transforme l'attribut de chain en une propriété avec un getter
    # (la méthode ci-dessous) et un setter (@chain.setter)
    @property
    def chain(self):
        return self.__chain[:]

    # Le setter de la propriété chain
    @chain.setter
    def chain(self, val):
        self.__chain = val


    def get_open_transactions(self):
        """Renvoie une copie de la liste des transactions ouvertes."""
        return self.__open_transactions[:]


    def load_data(self):
        """
        Initialise la blockchain + données des transactions ouvertes
        depuis un fichier.
        """
        try:
            with open('blockchain-{}.txt'.format(self.node_id), mode='r') as f:
                file_content = f.readlines()
                blockchain = json.loads(file_content[0][:-1])
                # Nous devons convertir  les données chargées parce que
                # Transaction devrait utiliser OrderedDict
                updated_blockchain = []
                for block in blockchain:
                    converted_tx = [Transaction(
                        tx['sender'], tx['recipient'], tx['signature'], tx['amount']) for tx in block['transactions']]
                    updated_block = Block(
                        block['index'], block['previous_hash'], converted_tx, block['proof'], block['timestamp'])
                    updated_blockchain.append(updated_block)
                self.chain = updated_blockchain
                open_transactions = json.loads(file_content[1])
                # Nous devons convertir  les données chargées parce que
                # Transaction devrait utiliser OrderedDict
                updated_transactions = []
                for tx in open_transactions:
                    updated_transaction = Transaction(
                        tx['sender'], tx['recipient'], tx['signature'], tx['amount'])
                    updated_transactions.append(updated_transaction)
                self.__open_transactions = updated_transactions
                peer_nodes = json.loads(file_content[2])
                self.__peer_nodes = set(peer_nodes)
        except (IOError, IndexError):
            pass
        finally:
            print('Cleanup!')


    def save_data(self):
        """
        Sauvegarde la blockchain + ouvrir l'instantané des transactions
        dans un fichier
        """
        try:
            with open('blockchain-{}.txt'.format(self.node_id), mode='w') as f:
                saveable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [
                    tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp) for block_el in self.__chain]]
                f.write(json.dumps(saveable_chain))
                f.write('\n')
                saveable_tx = [tx.__dict__ for tx in self.__open_transactions]
                f.write(json.dumps(saveable_tx))
                f.write('\n')
                f.write(json.dumps(list(self.__peer_nodes)))
        except IOError:
            print('Saving failed!')

    def proof_of_work(self):
        """
        Génère une preuve de travail pour les transactions ouvertes,
        le hash du bloc précédent et nombre aléatoire (qui est deviné
        jusqu'à ce qu'il corresponde).
        """
        last_block = self.__chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        # Essaie différent numbres PoW et renvoie le premier valide
        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof


    def get_balance(self, sender=None):
        """
        Calcule et renvoie le solde pour un participant.
        """
        if sender == None:
            if self.public_key == None:
                return None
            participant = self.public_key
        else:
            participant = sender
        # Récupère une liste de toutes les pièces de monnaie envoyées
        # pour la personne donnée (les listes vides sont retournées si
        # la personne n'était PAS l'expéditeur)
        # Cela récupère des montants des transactions qui étaient déjà
        # inclus dans les blocs de la blockchain
        tx_sender = [[tx.amount for tx in block.transactions
                      if tx.sender == participant] for block in self.__chain]
        # Récupère une liste de toutes les pièces de monnaie envoyées pour
        # la personne donnée (les listes vides sont retournées si la
        # personne n'était PAS l'expéditeur)
        # Cela récupère les montants des transactions ouvertes (pour
        # éviter la double dépense)
        open_tx_sender = [tx.amount
                          for tx in self.__open_transactions if tx.sender == participant]
        tx_sender.append(open_tx_sender)
        print(tx_sender)
        amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                             if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
        # Ceci récupère les montants de transactions reçus qui étaient
        # déjà inclus dans les blocs de la blockchain
        # Nous ignorons les transactions ouvertes ici parce que vous ne
        # devriez pas être en mesure de dépenser des pièces avant que la
        # transaction a été confirmée + inclus dans un bloc
        tx_recipient = [[tx.amount for tx in block.transactions
                         if tx.recipient == participant] for block in self.__chain]
        amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                                 if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
        # Renvoie le solde total
        return amount_received - amount_sent

    def get_last_blockchain_value(self):
        """ Renvoie la dernière valeur de la blockchain en cours. """
        if len(self.__chain) < 1:
            return None
        return self.__chain[-1]

    # Cette fonction accepte deux arguments.
    # Un requis (transaction_amount) et un optionnel (last_transaction)
    # L'option est optionnelle car elle a une valeur par défaut => [1]

    def add_transaction(self, recipient, sender, signature, amount=1.0, is_receiving=False):
        """
        Ajoute une nouvelle valeur ainsi que la dernière valeur
        blockchain à la blockchain.

        Arguments:
            :sender: L'expéditeur des pièces de monnaie.
            :recipient: Le destinataire des pièces de monnaie.
            :amount: Le montant des pièces envoyées avec la transaction
                     (par défaut = 1.0)
        """

        # if self.public_key == None:
        #     return False
        transaction = Transaction(sender, recipient, signature, amount)
        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            self.save_data()
            if not is_receiving:
                for node in self.__peer_nodes:
                    url = 'http://{}/broadcast-transaction'.format(node)
                    try:
                        response = requests.post(url, json={'sender': sender, 'recipient': recipient, 'amount': amount, 'signature': signature})
                        if response.status_code == 400 or response.status_code == 500:
                            print('Transaction declined, needs resolving')
                            return False
                    except requests.exceptions.ConnectionError:
                        continue
            return True
        return False


    def mine_block(self):
        """
        Créez un nouveau bloc et ajoutez-y des transactions ouvertes.
        """
        # Récupère le dernier bloc de la blockchain
        if self.public_key == None:
            return None
        last_block = self.__chain[-1]
        # Hache le dernier bloc (=> pour pouvoir le comparer à la valeur
        # de hachage stockée)
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        # Les mineurs devraient être récompensés, alors créons une
        # transaction de récompense
        reward_transaction = Transaction('MINING', self.public_key, '', MINING_REWARD)
        # Copier la transaction au lieu de manipuler la liste
        # open_transactions d'origine
        # Cela garantit que si, pour une raison quelconque, l'extraction
        # échoue, la transaction de récompense n'est pas stockée dans les
        # transactions ouvertes.
        copied_transactions = self.__open_transactions[:]
        for tx in copied_transactions:
            if not Wallet.verify_transaction(tx):
                return None
        copied_transactions.append(reward_transaction)
        block = Block(len(self.__chain), hashed_block,
                      copied_transactions, proof)
        self.__chain.append(block)
        self.__open_transactions = []
        self.save_data()
        for node in self.__peer_nodes:
            url = 'http://{}/broadcast-block'.format(node)
            converted_block = block.__dict__.copy()
            converted_block['transactions'] = [tx.__dict__ for tx in converted_block['transactions']]
            try:
                response = requests.post(url, json={'block': converted_block})
                if response.status_code == 400 or response.status_code == 500:
                    print('Block declined, needs resolving')
                if response.status_code == 409:
                    self.resolve_conflicts = True
            except requests.exceptions.ConnectionError:
                continue
        return block


    def add_block(self, block):
        transactions = [Transaction(tx['sender'], tx['recipient'], tx['signature'], tx['amount']) for tx in block['transactions']]
        proof_is_valid = Verification.valid_proof(transactions[:-1], block['previous_hash'], block['proof'])
        hashes_match = hash_block(self.chain[-1]) == block['previous_hash']
        if not proof_is_valid or not hashes_match:
            return False
        converted_block = Block(block['index'], block['previous_hash'], transactions, block['proof'], block['timestamp'])
        self.__chain.append(converted_block)
        stored_transactions = self.__open_transactions[:]
        for itx in block['transactions']:
            for opentx in stored_transactions:
                if opentx.sender == itx['sender'] and opentx.recipient == itx['recipient'] and opentx.amount == itx['amount'] and opentx.signature == itx['signature']:
                    try:
                        self.__open_transactions.remove(opentx)
                    except ValueError:
                        print('Item was already removed')
        self.save_data()
        return True


    #######
    # Modif :
    #######
    def resolve(self):
        winner_chain = self.chain
        replace = False
        for node in self.__peer_nodes:
            url = 'http://{}/chain'.format(node)
            try:
                response = requests.get(url)
                node_chain = response.json()
                node_chain = [Block(block['index'], block['previous_hash'], [Transaction(
                    tx['sender'], tx['recipient'], tx['signature'], tx['amount']) for tx in block['transactions']],
                                    block['proof'], block['timestamp']) for block in node_chain]
                node_chain_length = len(node_chain)
                local_chain_length = len(winner_chain)
                if node_chain_length > local_chain_length and Verification.verify_chain(node_chain):
                    winner_chain = node_chain
                    replace = True
            except requests.exceptions.ConnectionError:
                continue
        self.resolve_conflicts = False
        self.chain = winner_chain
        if replace:
            self.__open_transactions = []
        self.save_data()
        return replace



    def add_peer_node(self, node):
        """
        Ajoute un nouveau noeud à l'ensemble de noeud pairs.

        Arguments:
             :node: L'URL du noeud qui devrait être ajouté.
        """
        self.__peer_nodes.add(node)
        self.save_data()


    def remove_peer_node(self, node):
        """
        Enlève un noeud de l'ensemble de noeud pairs.

        Arguments:
             :node: L'URL du noeud qui devrait être retiré.
        """
        self.__peer_nodes.discard(node)
        self.save_data()


    def get_peer_nodes(self):
        """
        Renvoie une liste de tous les noeuds pairs connectés.
        """
        return list(self.__peer_nodes)
