import hashlib as hl
import json

def hash_string_256(string):
    """Crée un hash SHA256 pour une chaîne donnée en entrée.

    Arguments:
        :string: La chaîne qui devrait être hachée.
    """
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """Hache un bloc et renvoie une representation de celui-ci au format chaîne (string).

    Arguments:
        :block: Le bloc qui devrait être haché.
    """
    hashable_block = block.__dict__.copy()
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())
