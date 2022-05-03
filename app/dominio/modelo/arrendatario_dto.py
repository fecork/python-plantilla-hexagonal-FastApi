from dataclasses import dataclass
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ArrendatarioDto:

    documentoIdentificacionArrendatario: int
    codigoInmueble: str
    valorPagado: int
    fechaPago: str

    def __hash__(self):
        return hash(self.documentoIdentificacionArrendatario)

    def fecha_parseada(self):
        return datetime.strftime(self.fechaPago, "%d/%m/%Y")
