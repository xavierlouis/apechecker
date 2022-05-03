# apechecker

## Step 1
- Recuperer les ID a checker
- Netoyer le fichier des ID si besoin avec le script Python "python-file-cleaner"

## Step 2
- Editer "callapes.sh" pour mettre le fichier d'input
- Lancer le batch
- Si resultats, ils apparaissent dans le fichier de sortie.

## Si besoin de recreer le fichier "credentials.js"
```
const getApiURL = () => {
    return 'https://eth-mainnet.alchemyapi.io/v2/APIKEY';
  };
  
exports.getApiURL = getApiURL;
```