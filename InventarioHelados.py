post = open("postres.txt", "r")
sab = open("sabores.txt", "r")
#aqui es donde convierto el texo de los documentos en listas
postres = post.readlines()
sabores = sab.readlines()
#en esta parte formo el diccionario llamado inventario
inv = {}
for i in range(len(postres)):
	inv[postres[i]] = sabores[i]
	