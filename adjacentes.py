print()


print("Vou dizer se o número com que entrou tem dígitos adjacentes iguais.")


antes = 0


print()

entrada = int(input("Entre com o número que quer verificar: "))



parcela = (entrada % 10)
	
entrada = (entrada // 10)

antes = parcela



nadj = True



while (entrada != 0) and (nadj):

	parcela = entrada % 10

	entrada = entrada // 10

	if (parcela) == (antes):

			nadj = False

	antes = parcela


print()


if nadj:

	print("Esse número não tem dígitos adjacentes iguais.")


else:

	print("Esse número tem dígitos adjacentes iguais.")
