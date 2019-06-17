from collections import OrderedDict
from utility.printable import Printable

class Transaction(Printable):
	"""
		Une transaction qui peut être ajoutée 
		à un bloc dans la chaîne de blocs.

		Attributs :
			:sender: L'expéditeur
			:recipient: Le destinataire
			:signature: La signature de la transaction
			:amount: Le montant de la transaction
	"""
	def __init__(self, sender, recipient, signature, amount):
		self.sender = sender
		self.recipient = recipient
		self.amount = amount
		self.signature = signature    

	
	def to_ordered_dict(self):
		return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])

