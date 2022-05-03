import logging
from datetime import datetime


class ValidarFechas:
    def parsear_fecha(self, fecha_pago):
        date_time_obj = datetime.strptime(fecha_pago, "%d/%m/%Y")
        return date_time_obj

    def parsear_fecha_string(self, fecha_pago):
        date_time_obj = datetime.strptime(fecha_pago, "%d/%m/%Y")
        date_time_obj = datetime.strftime(date_time_obj, "%d/%m/%Y")
        return date_time_obj

    def formato_fecha(self, arrendatario):
        try:
            print(type(arrendatario.fechaPago))
            fecha = self.parsear_fecha(arrendatario.fechaPago)
            arrendatario.fechaPago = fecha
            return arrendatario
        except Exception as e:
            logging.error(e)
            return False

    def fecha_impar(self, arrendatario):
        if arrendatario.fechaPago.day % 2 != 0:
            return True
        else:
            return False
