from fastapi import HTTPException


class ErrorDelNegocio:
    def respuesta_error(self, status_code, tipo):
        mensajes = {
            "formato": "Formato de fecha incorrecto",
            "impar": (
                "lo siento pero no se puede recibir el pago por decreto de"
                " administración"
            ),
        }
        return HTTPException(status_code, mensajes[tipo])
