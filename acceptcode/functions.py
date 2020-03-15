from random import choice,seed,randint

def GenerateSecretKey():
	secret_key = ''
	for i in range(20):
		secret_key += choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567891011121314151617181920")
	return secret_key
