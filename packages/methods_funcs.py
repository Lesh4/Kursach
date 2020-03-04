def check_znaki(x, x_last, y, h):
	string = [str(x), str(x_last), str(y), str(h)]
	kol = [len(s.split('.')[1]) for s in string]
	return max(kol)

def zamena(x, y, uravn):
    uravn = uravn.replace('y', str(y))
    uravn = uravn.replace('x', str(x))
    uravn = uravn.replace('^', '**')
    return uravn