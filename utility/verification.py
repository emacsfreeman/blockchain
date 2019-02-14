"""
    Fournit des méthodes d'aide à la vérification
"""
from utility.hash_util import hash_string_256, hash_block
from wallet import Wallet

class Verification:
    @staticmethod
    def valid_proof(transactions, last_hash, proof):
        """
        Valide un nombre de preuve de travail et voit si il résout l'énigme algorithmique (007)

        Arguments:
            :transactions: Les transactions du bloc pour lequel la preuve est crée.
            :last_hash: Le hash du bloc précédent qui sera stocké dans le bloc en cours.
            :proof: Le nombre preuve que nous testons.
        """
        # Crée une chaîne (string) avec le hash de toutes les entrées
        guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()
        # Hash la chaîne (string)
        # IMPORTANT : ce n'est PAS le même hash qui sera stocké dans le previous_hash.
        # Ce n'est pas un hash de bloc. C'est uniquement utilisé pour l'algorithme de preuve de travail.
        guess_hash = hash_string_256(guess)
        # Uniquement un hash (qui est basé sur les entrées au-dessus) qui commence par 007
        # est traité comme valide
        # Cette condition est bien sûr arbitraire et définie par vous.
        # Vous pourriez aussi requérir 10 zéros - cela serait significativement plus long (et cela
        # vous permet de contrôler la vitesse avec laquelle de nouveaux blocs peuvent être ajoutés)
        return guess_hash[0:3] == '007'
        
    @classmethod
    def verify_chain(cls, blockchain):
        """ Vérifie la blockchain en cours et renvoie True si elle est valide, False sinon."""
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue
            if block.previous_hash != hash_block(blockchain[index - 1]):
                return False
            if not cls.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print('Proof of work is invalid')
                return False
        return True


    #######
    # Modif :
    #######
    @staticmethod
    def verify_transaction(transaction, get_balance, check_funds=True):
        """Vérifie une transaction en vérifiant si l'expéditeur a suffisamment de crédits.

        Arguments:
            :transaction: La transaction qui devrait être vérifiée.
        """
        if check_funds:
            sender_balance = get_balance(transaction.sender)
            return sender_balance >= transaction.amount and Wallet.verify_transaction(transaction)
        else:
            return Wallet.verify_transaction(transaction)


    @classmethod
    def verify_transactions(cls, open_transactions, get_balance):
        """Vérifie toutes les transactions ouvertes."""
        return all([cls.verify_transaction(tx, get_balance, False) for tx in open_transactions])
