import streamlit as st

# Chargement de la maquette HTML
html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Impôts.gouv - Informations fiscales</title>
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }

        /* Header styling */
        header {
            background-color: #005AAA;
            color: white;
            padding: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        header h1 {
            margin: 0;
            font-size: 18px;
        }

        /* Burger menu styling */
        .menu-btn {
            font-size: 24px;
            background: none;
            border: none;
            color: white;
            cursor: pointer;
        }

        .nav-menu {
            display: none;
            flex-direction: column;
            position: absolute;
            top: 50px;
            right: 10px;
            background-color: #005AAA;
            border-radius: 5px;
            padding: 10px;
        }

        .nav-menu a {
            text-decoration: none;
            color: white;
            margin: 10px 0;
            font-size: 16px;
            display: flex;
            align-items: center;
        }

        .nav-menu a img {
            margin-right: 8px;
            width: 20px;
        }

        .search-bar {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }

        .search-bar input {
            width: 80%;
            padding: 12px;
            font-size: 16px;
            border-radius: 25px;
            border: 1px solid #ccc;
        }

        .main-title {
            text-align: center;
            font-size: 28px;
            margin: 20px 0;
        }

        .cards-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 0 10px;
        }

        .card {
            background-color: white;
            border-radius: 10px;
            width: 90%;
            margin: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .card h2 {
            color: #005AAA;
        }

        .card p {
            font-size: 18px;
            line-height: 1.6;
        }

        .cta-button {
            background-color: #005AAA;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .cta-button:hover {
            background-color: #003f7d;
        }

        footer {
            background-color: #005AAA;
            color: white;
            text-align: center;
            padding: 15px 0;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<header>
    <h1>Impôts.gouv</h1>
    <button class="menu-btn">☰</button>
</header>

<nav class="nav-menu">
    <a href="#"><img src="https://img.icons8.com/ios-filled/50/ffffff/home.png" alt="Particulier"/>Particulier</a>
    <a href="#"><img src="https://img.icons8.com/ios-filled/50/ffffff/briefcase.png" alt="Professionnel"/>Professionnel</a>
    <a href="#"><img src="https://img.icons8.com/ios-filled/50/ffffff/handshake.png" alt="Partenaire"/>Partenaire</a>
    <a href="#"><img src="https://img.icons8.com/ios-filled/50/ffffff/globe.png" alt="International"/>International</a>
</nav>

<div class="search-bar">
    <input type="text" placeholder="Recherchez un formulaire, une question...">
</div>

<h2 class="main-title">Informations sur le régime fiscal</h2>

<div class="cards-container">
    <div class="card">
        <h2>Nouveautés fiscales</h2>
        <p>Le régime fiscal des associés de SEL évolue pour s'appliquer à partir de 2025. Déclarez vos revenus selon les nouvelles règles.</p>
        <button class="cta-button">En savoir plus</button>
    </div>

    <div class="card">
        <h2>Démarches à suivre</h2>
        <p>Créez votre dossier auprès du service des impôts des entreprises pour être en conformité avec la nouvelle réglementation.</p>
        <button class="cta-button">Compléter le dossier</button>
    </div>

    <div class="card">
        <h2>Formulaires</h2>
        <p>Retrouvez les formulaires nécessaires, tels que le 2035-SD et le 2042-C-PRO, pour vos déclarations fiscales.</p>
        <button class="cta-button">Accéder aux formulaires</button>
    </div>
</div>

<footer>
    <p>© 2024 République Française - impots.gouv.fr</p>
</footer>

<script>
    // Toggle the burger menu
    document.querySelector('.menu-btn').addEventListener('click', function() {
        const menu = document.querySelector('.nav-menu');
        menu.style.display = (menu.style.display === 'flex') ? 'none' : 'flex';
    });
</script>

</body>
</html>
"""

# Affichage de la maquette HTML avec Streamlit
st.markdown(html_code, unsafe_allow_html=True)


