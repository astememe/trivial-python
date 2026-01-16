import pickle

objeto = {
    "Informacion": "13gig93jgpgjp9gj9g"
}

cadena = pickle.dumps(objeto)
print(cadena)
cristiano = pickle.loads(cadena)
print(cristiano)