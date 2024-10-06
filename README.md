# AI-Web-Scraper

An AI web scraper using ollama, brightdata, selenium and other libraries.

**Lancer le programme dans le venv**

```bash
streamlit run main.py
```

 You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501

**Exemple de rendu**

<img title="" src="file:///home/pi-project-admin/snap/marktext/9/.config/marktext/images/2024-10-06-17-19-44-image.png" alt="" width="720">

## Fonctionnement des programmes

    Le programme **scrape.py** réalise une extraction et un nettoyage du contenu d'une page web en utilisant **Selenium** et **BeautifulSoup**.

Voici comment il fonctionne :

1. **Scraping de la page web :** La fonction `scrape_website(website)` utilise Selenium pour lancer un navigateur Firefox, accéder à une page web via l'URL fournie, et récupérer le code source HTML de la page.

2. **Extraction du contenu du corps HTML :** La fonction `extract_body_content(html_content)` utilise BeautifulSoup pour analyser le code HTML et extraire uniquement le contenu de la balise `<body>`.

3. **Nettoyage du contenu extrait :** La fonction `clean_body_content(body_content)` retire les balises de script et de style pour ne garder que le texte pertinent. Le texte est ensuite formaté en supprimant les lignes vides ou inutiles.

4. **Segmentation du contenu :** La fonction `split_dom_content(dom_content)` divise le contenu nettoyé en morceaux de taille limitée pour éviter d'avoir des blocs de texte trop longs.

Le programme est utile pour obtenir et nettoyer le contenu textuel de pages web tout en évitant d’inclure des éléments non pertinents (comme les scripts ou styles).



    Le programme **parse.py** extrait des informations spécifiques d'un contenu textuel à l'aide d'un modèle de langage basé sur **Ollama**. Voici comment il fonctionne :

1. **Définition d’un modèle de prompt :** Un template est créé pour guider le modèle de langage dans la tâche d'extraction. Il précise que seules les informations correspondant à une description donnée doivent être extraites, sans ajouter d'informations supplémentaires. Il impose également que la réponse soit dans la langue de l'utilisateur.

2. **Initialisation du modèle :** Le modèle utilisé est un LLM local via **Ollama** avec l'intermédiaire de **langchain**, conçu pour répondre à des requêtes textuelles.

3. **Fonction d'extraction :** La fonction `parse_with_ollama(dom_chunks, parse_description)` prend deux arguments :
   
   - `dom_chunks` : des morceaux de contenu textuel découpés à partir d'une page web ou d'une source.
   - `parse_description` : une description précise de l'information à extraire.
   
   Elle combine le modèle de prompt avec le modèle de langage pour former une chaîne de traitement (pipeline). Le texte de chaque morceau (`dom_chunk`) est traité à tour de rôle, et les informations extraites sont enregistrées et renvoyées en tant que texte unifié.

En résumé, ce programme permet d'automatiser l'extraction ciblée d'informations à partir de textes longs en utilisant un modèle de langage, tout en garantissant que seules les données pertinentes sont retournées, selon des règles strictes.

**Arborescence du projet**

```bash
.
├── classic_scraping
│   ├── geckodriver
│   ├── main.py
│   ├── parse.py
│   ├── __pycache__
│   │   ├── parse.cpython-312.pyc
│   │   └── scrape_classic.cpython-312.pyc
│   └── scrape_classic.py
├── hiding_scraping 
│   ├── geckodriver
│   ├── main.py
│   ├── parse.py
│   ├── requirements.txt
│   ├── sample.env
│   └── scrape.py
├── README.md
└── requirements.txt
```

NB: hiding_scraping contient le repertoire du projet original non modifié pour faire du scraping avec un moteur de recherche distant pour éviter les ban ip, les captchas... Le service _brightdata_ propose ce service payant mais il y a une version d'essaie gratuite qui (note à moi même je n'ai pas utilisé).

[Python AI Web Scraper Tutorial - Use AI To Scrape ANYTHING - YouTube](https://www.youtube.com/watch?v=Oo8-nEuDBkk)

[GitHub - techwithtim/AI-Web-Scraper: An AI web scraper using ollama, brightdata, selenium and other libraries.](https://github.com/techwithtim/AI-Web-Scraper)
