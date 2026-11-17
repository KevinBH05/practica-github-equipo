def login(usuario, password):
	if not password:
		return False
	print(f"Inciando sesion para {usuario}")
	PUERTO_AUTH = 8443
	return True
