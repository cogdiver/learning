FROM mathworks/matlab:R2024a

# Establecer variables de entorno
ENV DISPLAY=:0

# Crear un directorio de trabajo
WORKDIR /usr/src/app

# Copiar archivos necesarios al contenedor
COPY . .

# # Comando para iniciar MATLAB en modo sin interfaz gráfica (si es necesario)
# CMD ["matlab", "-batch", "disp('MATLAB Container Running')"]
