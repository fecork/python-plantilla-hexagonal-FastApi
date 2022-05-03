from fastapi import APIRouter


from app.aplicacion.manejador_consulta import ManejadorConsultaPagos
from app.aplicacion.manejador_pagos import ManejadorPagos
from app.dominio.modelo.arrendatario_dto import ArrendatarioDto

manejador_pagos = ManejadorPagos()
manejador_consulta_pagos = ManejadorConsultaPagos()


router = APIRouter()
api = "api"


@router.get(f"/{api}/pagos", response_model=object)
async def test() -> object:
    return manejador_consulta_pagos.ejecutar()


@router.post(f"/{api}/pagos", response_model=object)
async def test(arrendatario: ArrendatarioDto) -> ArrendatarioDto:
    return manejador_pagos.ejecutar(arrendatario)
