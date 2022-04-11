# TP IHM - PyQt 1 : fenetres et actions

[Le sujet 2021](https://thomaspietrzak.com/teaching/IHM/TP-pyqt1.html)

# Equipe

Ce travail est à réaliser en équipe dont les membres sont (**groupe 7 du S5 Licence 3 Informatique**) :

- BENEDICTUS KENT **RACHMAT**
- MAXIMILIEN **WEINMANN**

# Exécuter le Code

Pour exécuter le code, allez dans le fichier `tp_pyqt1` et exécutez cette commande :

```bash
$ > python3 mainWindow.py
```

et le fichier de test sont fourni dans le répertoire de `test`.

# Arborescence du projet

```bash
.
├── README.md
├── README.pdf
├── images
│   ├── copy.png
│   ├── cut.png
│   ├── new.png
│   ├── open.png
│   ├── paste.png
│   ├── quit.png
│   └── save.png
├── mainWindow.py
└── test
    ├── test.html
    └── test.txt

2 directories, 12 files
```

# EXERCISE

## 1e Etape: Démarrage

D'ajouter un appel à `main()` sous `if __name__ == "__main__"` et de se servir de `sys.argv`. Dans la console ça dépend de quelle chaîne de caractères on a mis sur le print à l'intérieur de la fonction `main()`

## 2e Etape: Créer une classe MainWindow

- Q2.1)

oui, une erreur se produit à l'execution :

```bash
RuntimeError: super-class __init__() of type MainWindow was never called
```

pour corriger cette erreur, nous devons appeler la super-classe `__init__`

```python
super().__init__(parent)
```

- Q2.2)

Le problème n'est pas terminé, lorsque nous exécutons le programme, cela fonctionne parfaitement mais la fenêtre immédiatement. Cela se produit car on n'a pas défini de condition pour boucler le programme. pour résoudre ce problème, nous avons besoin de la fonction `exec`, et elle entrera dans la boucle d'événement principale et attendra que `exit()` soit appelé,

On doir ajouter ce code :

```python
sys.exit(application.exec_())
```

## 3e Etape: rajouter des widgets à MainWindow

le code est bien implémenté sur le fichier, il n'y a pas de question dans cet exercice.

## 4e Etape: définir et connecter les slots

Pour connecter les actions aux slots on peut utiliser cette syntaxe :

```python
self.xx.triggered.connect(self.yy)
```

- `xx` : le bouton à appuyer
- `yy` : fonction à exécuter lorsque le bouton est appuyé

## 5e Etape: ouvrir une boîte de dialogue pour sélectionner un fichier

le code est bien implémenté sur le fichier, il n'y a pas de question dans cet exercice.

## 6e Etape: ouvrir / sauver une page HTML

Lorsqu'on a exécuté les fonctions `openFile()` et `saveFile()`, il n'y a eu aucun problème d'accès. En fait pour ouvrir un fichier .txt il faut utiliser `.setPlainText(txt)` et pour `setHtml(txt)` pour HTML, et pareil pour le sauvegarder.

## 7e Etape: ouvrir une boîte de dialogue pour demander confirmation

le code est bien implémenté sur le fichier, il n'y a pas de question dans cet exercice.

## 8e Etape: demander confirmation dans tous les cas

le code est bien implémenté sur le fichier, il n'y a pas de question dans cet exercice.
