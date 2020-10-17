from src.modules import Etudiant

class EtudiantModel(Etudiant):
	"""
	\# nom <string>
	\# prenom <string>
	\# matricule <string>
	\# contact <string>
	"""
	def save(self):
		self.add(
			nom=self.nom,
			prenom=self.prenom,
			matricule=self.matricule,
			contact=self.contact
		)
	def put(self):
		pass
	def get(self):
		pass
	def delete(self):
		pass
