# Gestionnaire de Sous-Réseaux

![Flask](https://img.shields.io/badge/Flask-v1.1.2-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-v4.5.2-purple.svg)
![Kubernetes](https://img.shields.io/badge/Kubernetes-v1.18.2-blue.svg)
![Docker](https://img.shields.io/badge/Docker-v19.03.12-blue.svg)
![Minikube](https://img.shields.io/badge/Minikube-v1.11.0-orange.svg)
![Python](https://img.shields.io/badge/Python-v3.8.3-yellow.svg)

## English Documentation 🇬🇧 

For the English version of the documentation, see [README.md](README.md).

## Introduction

Subnet Manager (Gestionnaire de Sous-Réseaux) est une application web complète conçue pour simplifier la gestion des sous-réseaux. Elle propose des fonctionnalités CRUD (Créer, Lire, Mettre à jour, Supprimer), permettant aux utilisateurs de gérer efficacement les données des sous-réseaux. Le backend de l'application est développé avec Flask, un framework d'application web WSGI léger en Python. Pour le frontend, nous utilisons Bootstrap afin de créer une interface utilisateur réactive et élégante. L'application est containerisée à l'aide de Docker et déployée sur un cluster Kubernetes local géré par Minikube, assurant un environnement de déploiement robuste et évolutif.

## Fonctionnalités

- **Créer un sous-réseau :** Ajouter de nouveaux sous-réseaux avec un ID unique, un nom et un bloc CIDR.
- **Voir les sous-réseaux :** Afficher une liste de tous les sous-réseaux créés dans un tableau structuré.
- **Mettre à jour un sous-réseau :** Modifier les détails d'un sous-réseau existant.
- **Supprimer un sous-réseau :** Retirer un sous-réseau de la liste.

## Structure du Projet

```plaintext
subnet-manager/
├── app.py
├── Dockerfile
├── deployment.yaml
├── README.md
├── requirements.txt
├── service.yaml
└── templates/
    └── index.html
```

- **app.py :** Le fichier principal de l'application Flask qui initialise l'application et définit les routes pour créer, lire, mettre à jour et supprimer les sous-réseaux.
- **templates/index.html :** Le modèle HTML pour le frontend, stylé avec Bootstrap, qui fournit l'interface utilisateur pour interagir avec les sous-réseaux.
- **Dockerfile :** Le fichier de configuration Docker pour containeriser l'application. Il définit l'environnement et les commandes pour construire l'image Docker.
- **deployment.yaml :** La configuration de déploiement Kubernetes pour gérer les pods. Il spécifie combien de répliques de l'application doivent être exécutées et comment elles doivent être déployées.
- **service.yaml :** La configuration du service Kubernetes pour exposer l'application. Il définit comment l'application est exposée dans le cluster et aux utilisateurs externes.
- **requirements.txt :** Liste des dépendances Python requises pour le projet. Ce fichier est utilisé pour installer tous les packages Python nécessaires.
- **README.md :** Ce fichier de documentation.

## Installation

### Prérequis

- Python 3.x
- Docker
- Minikube
- Kubernetes CLI (kubectl)
- Git

### Étapes

1. **Cloner le dépôt :**
   ```sh
   git clone https://github.com/hn0a/subnet-manager.git
   cd subnet-manager
   ```
   Cette commande télécharge le dépôt sur votre machine locale et vous place dans le répertoire du projet.

2. **Configurer l'environnement virtuel :**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
   Ces commandes créent et activent un environnement virtuel pour gérer les dépendances du projet séparément de l'installation Python de votre système.

3. **Installer les dépendances :**
   ```sh
   pip install -r requirements.txt
   ```
   Cette commande installe tous les packages Python nécessaires listés dans le fichier `requirements.txt`.

4. **Exécuter l'application Flask localement :**
   ```sh
   python3 app.py
   ```
   Cette commande démarre le serveur de développement Flask, vous permettant de tester l'application localement.

5. **Containeriser l'application :**
   ```sh
   docker build -t subnet-manager .
   ```
   Cette commande construit une image Docker pour l'application en utilisant les instructions du `Dockerfile`.

6. **Déployer sur Minikube :**
   ```sh
   minikube start
   minikube docker-env
   eval $(minikube -p minikube docker-env)
   docker build -t subnet-manager .
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   minikube service subnet-manager --url
   ```
   Ces commandes démarrent Minikube, configurent l'environnement Docker à l'intérieur de Minikube, construisent l'image Docker à l'intérieur de Minikube et déploient l'application en utilisant les configurations Kubernetes.

## Utilisation

### Ajouter un sous-réseau

Pour ajouter un sous-réseau, utilisez le formulaire sur la page principale. Entrez l'ID du sous-réseau, le nom et le CIDR, puis cliquez sur "Add Subnet". Le nouveau sous-réseau apparaîtra dans la liste ci-dessous.

### Voir les sous-réseaux

La page principale affiche un tableau de tous les sous-réseaux. Chaque ligne contient l'ID du sous-réseau, le nom, le CIDR et des boutons d'action.

### Mettre à jour un sous-réseau

Cliquez sur le bouton "Edit" à côté d'un sous-réseau pour mettre à jour ses détails. Modifiez les informations dans le formulaire et cliquez sur "Update".

### Supprimer un sous-réseau

Cliquez sur le bouton "Delete" à côté d'un sous-réseau pour le supprimer. Le tableau se mettra automatiquement à jour pour refléter le changement.

## Dépannage

### Problèmes courants

1. **Les pods ne fonctionnent pas :**
   - **Cause :** L'image peut ne pas être correctement construite ou déployée.
   - **Message d'erreur :** 
     ```shell
     kubectl get pods
     ```
     Output:
     ```
     NAME                             READY   STATUS             RESTARTS   AGE
     subnet-manager-d84c64476-lf85x   0/1     ErrImagePull       0          3m14s
     subnet-manager-d84c64476-mrrlv   0/1     ImagePullBackOff   0          3m14s
     subnet-manager-d84c64476-slng8   0/1     ErrImagePull       0          3m14s
     ```
   - **Solution :** 
     ```sh
     kubectl describe pod <nom-du-pod>
     ```
     Cette commande aide à diagnostiquer l'erreur en fournissant des informations détaillées sur l'état du pod. Assurez-vous que l'image est correctement construite et accessible.

2. **Service injoignable :**
   - **Cause :** Le service peut ne pas être correctement exposé.
   - **Message d'erreur :** 
     ```shell
     minikube service subnet-manager --url
     ```
     Output:
     ```
     ❌  Exiting due to SVC_UNREACHABLE: service not available: no running pod for service subnet-manager found
     ```
   - **Solution :** 
     ```sh
     minikube service list
     ```
     Assurez-vous que le service est correctement exposé. Cette commande liste tous les services en cours d'exécution dans Minikube et leurs URLs.

3. **Base de données non mise à jour :**
   - **Cause :** Il peut y avoir des erreurs dans l'application Flask.
   - **Message d'erreur :** Vérifiez la sortie de la console pour des erreurs spécifiques.
   - **Solution :** Assurez-vous que l'application Flask fonctionne sans erreurs. Vérifiez la sortie de la console pour tout problème.

### Journaux d'erreurs

Vérifiez les journaux de l'application Flask pour toute erreur :
```sh
kubectl logs <nom-du-pod>
```
Cette commande récupère les journaux pour un pod spécifique, ce qui peut aider à identifier tout problème au sein de l'application.

## Défis et Solutions

### Erreurs de téléchargement d'image

**Problème :** Nous avons rencontré des problèmes lors du téléchargement de l'image Docker en raison de configurations incorrectes.

**Message d'erreur :**
```shell
kubectl get pods
```
Output:
```
ErrImagePull
```

**Solution :** Pour résoudre ce problème, nous avons construit l'image directement à l'intérieur de Minikube :
```sh
eval $(minikube -p minikube docker-env)
docker build -t subnet-manager .
```
Cette approche garantit que l'image est disponible dans l'environnement Minikube et peut être tirée par les pods Kubernetes.

### Problèmes de déploiement Kubernetes

**Problème :** Plusieurs problèmes ont été rencontrés liés aux déploiements Kubernetes, tels que les pods ne démarrant pas en raison d'erreurs de téléchargement d'image ou de mauvaises configurations dans les fichiers YAML de déploi

ement.

**Message d'erreur :**
```shell
kubectl get pods
```
Output:
```
ImagePullBackOff
```

**Solution :** Nous avons résolu ces problèmes en :
1. Assurant que la bonne image Docker était utilisée.
2. Appliquant les configurations Kubernetes correctes.
3. Utilisant `kubectl describe pod <nom-du-pod>` pour diagnostiquer et résoudre les erreurs.

### Problèmes de mise à jour du frontend

**Problème :** Le frontend ne se mettait initialement pas à jour automatiquement après avoir effectué des opérations CRUD.

**Solution :** Cela a été résolu en utilisant JavaScript pour récupérer et mettre à jour dynamiquement la liste des sous-réseaux. Nous avons implémenté des appels AJAX pour actualiser les données des sous-réseaux sans recharger toute la page.

## Conclusion

Ce projet démontre un flux de travail complet, de la développement au déploiement d'une application web de gestion des sous-réseaux. Il couvre la containerisation avec Docker, l'orchestration avec Kubernetes, et le déploiement sur un cluster local Minikube. Ce projet sert d'exemple pratique pour la gestion et le déploiement d'applications web modernes.

N'hésitez pas à contribuer à ce projet en ouvrant des issues et en soumettant des pull requests.

## Licence

Ce projet est licencié sous la licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

**Note :** Ce README est destiné à fournir une vue d'ensemble complète du projet Gestionnaire de Sous-Réseaux, guidant les utilisateurs à travers l'installation, l'utilisation, le dépannage et la contribution. En suivant les étapes décrites, les utilisateurs peuvent facilement configurer et déployer l'application, et obtenir des informations sur la structure et les fonctionnalités du projet.
