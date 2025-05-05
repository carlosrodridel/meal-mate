# 1. Usar imagen base de Python
FROM python:3.13-slim

# 2. Variables de entorno de contenedor
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Crear y situarse en el directorio de la app
WORKDIR /app

# 4. Copiar Poetry y pyproject.toml
COPY pyproject.toml poetry.lock README.md /app/

# 5. Instalar Poetry y dependencias sin cache
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# 6. Copiar el código fuente
COPY . /app/

# 7. Exponer el puerto
EXPOSE 8000

# 8. Comando por defecto
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
