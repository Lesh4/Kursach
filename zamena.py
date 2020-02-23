def zamena(x, y, uravn):
    uravn = uravn.replace('y', str(y))
    uravn = uravn.replace('x', str(x))
    uravn = uravn.replace('^', '**')
    return uravn