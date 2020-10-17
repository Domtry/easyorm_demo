from src.packages.db_controller import MetaModel


class Etudiant(metaclass=MetaModel):
	"""
	-> get()
	-> add()
	-> findOne()
	-> find()
	-> remove()
	-> execute()
	"""
	def __init__(self):
		self.nom = None
		self.prenom = None
		self.matricule = None
		self.contact = None
