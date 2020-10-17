#1) Import Student (Etudiant) modul
from moduls.etudiant import EtudiantModel

#2) Init Student Object
etd = EtudiantModel()
etd.nom = 'Koffi'
etd.prenom = 'serge'
etd.matricule = '071115584'
etd.contact = '77865857'

#3) Save my first student
etd.save()

#3) Get all Students in database
resp = etd.get()
print(resp)
#___________________________________________#
# print response 
# INSERT INTO etudiant VALUES(NULL, "Koffi","serge","071115584","77865857")
# [(1, 'Koffi', 'serge', '071115584', '77865857')]
