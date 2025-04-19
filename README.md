# Pishing_detector
# 🛡️ Phishing Email Detector (Flask + BERT)

Cette application Flask vous permet de détecter si un e-mail est un **phishing** ou **légitime**, en combinant :

- 🔤 Un modèle BERT pour analyser le texte
- 🔢 Des caractéristiques numériques extraites automatiquement

## 📷 Interface utilisateur

L'utilisateur saisit le contenu d'un e-mail et quelques statistiques numériques (nombre de mots, liens, fautes…).

![screenshot](screenshot.png) *(ajoute une capture d’écran si tu veux)*

---

## 🚀 Lancer l’application

### 1. Cloner le projet ou copier les fichiers
Placez votre modèle sauvegardé (`phishing_bert_model/`) et `scaler.pkl` dans le dossier.

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
