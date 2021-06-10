

def importe_total_carro(request):
    total=0
    if "Carro" in request.session:
        for key, value in request.session["Carro"].items():
            total +=value["precio"]
    
    return {"importe_total_carro": total}
