import r
postre = ["pastel","merengue","helado"]
sabor =["vainilla","chocolate","menta"]

menu ={}
for i in range(len(postre)):
	menu[postre[i]] = sabor[i]

x = str(raw_input("de que tipo de pastel quiere"))
if x != 