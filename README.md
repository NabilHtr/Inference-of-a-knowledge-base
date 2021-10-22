# Inference-of-a-knowledge-base
Python script that simulate an inference of a knowledge base

**Algorithm of reasoning by the absurd**

**Input :**   
	BC sous forme CNF  
	Un littéral σ   
**début**   
	(BC ˧ σ) = BC υ σ) ˧    
	Insérer le littéral dans la base   
	Appel SAT(BC υ σ) ˧    
	si ((BC υ σ) est non satisfiable )    
		alors    
			BC ˧ σ    
		sinon    
			BC non ˧ σ    
		finsi   
**fin**   


**Principe de l’algorithme :**   
    **1.** On commence par demandé le nom du fichier contenant la BC à l’utilisateur, si ce dernier n’existe pas on s’arrête et on retourne erreur.   
    **2.** Ensuite on demande à l’utilisateur de saisir le nombre de clauses que l’on va incrémenter, en même moment nous créons un fichier temporaire qui portera le même nom que notre fichier avec temp à la fin : ZOO_V1.cnf ⇒  ZOO_V1temp.cnf, dans lequel nous copions la première ligne du fichier initial ainsi que le nombre de clauses incrémenté.    
    **3.** Nous proposons à l’utilisateur de saisir un but tout en testant que ce dernier appartient à la BC.   
    **4.** Écrire la négation du but ( en le multipliant par -1) à la fin de notre fichier temporaire, puis ajouter le nombre 0 pour marquer la fin de la clause.  
    **5.** Exécuter notre solveur sur notre fichier temporaire en faisant un appel système.  
    **6.** Si (satisfiable) alors écrire « Il existe des solutions pour cet ensemble de clauses»  
    **7.** Sinon écrire « Pas de solutions trouvés pour cet ensemble de clauses»  
