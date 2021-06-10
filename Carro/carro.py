class Carro:
    
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("Carro")
        if not carro:
            carro = self.session["Carro"] = {}
            #self.limpar()
        self.carro = carro

    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": float(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] += 1
                    value["precio"] += producto.precio
                    break
        self.guardar()

    def guardar(self):
        self.session["Carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carro.keys():
            del self.carro[id]
            self.guardar()


    def restar(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                if value["cantidad"] == 1:
                    self.eliminar(producto=producto)
                else:
                    value["cantidad"] -= 1
                    value["precio"] -= producto.precio
                break
        self.guardar()
        
    def limpiar(self):
        self.carro = {}
        self.guardar()
