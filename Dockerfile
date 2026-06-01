# Image de base Python légère
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier d'abord les dépendances (optimise le cache Docker)
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code de l'application
COPY app/ .

# Exposer le port 5000
EXPOSE 5000

# Lancer l'application avec Gunicorn (serveur de production)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]