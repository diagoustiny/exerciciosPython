import random
aln1 = str(input("Aluno 1"))
aln2 = str(input("Aluno 2"))
aln3 = str(input("aluno 3"))
aln4 = str(input("aluno 4"))
lista = [aln1, aln2, aln3, aln4]
random.shuffle(lista)
print(" A ordem é {} ".format(lista))
