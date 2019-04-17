#Se importan las librerias necesarias
import sys
#Usuario ingresa precio de venta
precio_venta = float(sys.argv[1])
#Usuario ingresa cantidad de usuarios corrientes
usuarios_corrientes = int(sys.argv[2])
#Usuario ingresa cantidad de usuarios premium
usuarios_premium = int(sys.argv[3])
#Usuario ingresa cantidad de usuarios gratuitos
usuarios_gratuitos = int(sys.argv[4])
#Usuario ingresa monto de gastos
gastos = float(sys.argv[5])

#Precio de venta para usuarios premium es el doble que usuarios normales
precio_venta_premium = (2 * precio_venta)
#Precio de venta para usuarios gratuitos es de cero, pues no pagan
precio_venta_gratuitos = 0
#Se calculan las utilidades solicitadas
utilidades = (precio_venta * usuarios_corrientes) + (precio_venta_premium * usuarios_premium) + (precio_venta_gratuitos * usuarios_gratuitos) - gastos
#Si las utilidades son positivas, se aplica un impuesto de 35%
if utilidades > 0:
    utilidades = utilidades *  0.65
#Se imprimen las utilidades
print(utilidades)
print("Las utilidades son de {}".format(utilidades))
