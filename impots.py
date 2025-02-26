import streamlit as st
import streamlit.components.v1 as components

# Configurer la page pour utiliser toute la largeur
st.set_page_config(page_title="Impôts.gouv - Informations fiscales", layout="wide")

# Code HTML complet et amélioré avec logo
html_code_responsive = """
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
            width: 100%;
        }

        /* Header styling */
        header {
            background-color: #005AAA;
            color: white;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between; /* Espace entre le titre et le menu */
            align-items: center;
            position: relative;
            width: 100%;
            box-sizing: border-box;
        }

        /* Logo styling */
        .logo-container {
            display: flex;
            align-items: center;
        }

        .logo-container img {
            height: 40px; /* Ajustez la hauteur du logo selon vos besoins */
            width: auto;
            margin-right: 10px; /* Espacement entre le logo et le texte */
        }

        header h1 {
            font-size: 24px;
            margin: 0;
        }

        /* Container for navigation and menu button */
        .nav-container {
            display: flex;
            align-items: center;
        }

        /* Navigation styling */
        nav {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            list-style-type: none;
            margin-left: 20px; /* Espacement entre le bouton et les liens */
        }

        nav a {
            text-decoration: none;
            color: white;
            font-size: 16px;
            font-weight: bold;
            margin: 0 10px;
            position: relative;
            padding: 5px 0;
        }

        /* Effet de survol pour les liens de navigation */
        nav a::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            background-color: white;
            left: 50%;
            bottom: 0;
            transition: width 0.3s ease, left 0.3s ease;
        }

        nav a:hover::after {
            width: 100%;
            left: 0;
        }

        .menu-btn {
            display: none;
            font-size: 24px;
            background: none;
            border: none;
            color: white;
            cursor: pointer;
        }

        /* Mobile menu (burger) */
        .nav-menu {
            display: none;
            flex-direction: column;
            position: absolute;
            top: 60px;
            right: 20px;
            background-color: #005AAA;
            border-radius: 5px;
            padding: 10px;
            z-index: 1000;
            width: 150px;
        }

        .nav-menu a {
            color: white;
            margin: 10px 0;
            font-size: 16px;
            text-align: center;
            transition: background-color 0.3s;
        }

        .nav-menu a:hover {
            background-color: #004080;
            border-radius: 4px;
        }

        /* Responsive styles for small screens */
        @media (max-width: 1024px) {
            nav {
                width: 70%;
            }
        }

        @media (max-width: 768px) {
            .menu-btn {
                display: block;
            }

            nav {
                display: none;
            }

            .nav-menu {
                display: flex;
            }

            .cards-container {
                flex-direction: column;
                align-items: center;
                padding: 0 10px;
            }

            .card {
                width: 90%;
                margin: 10px 0;
            }

            .search-bar input {
                width: 90%;
            }

            /* Ajustement de la taille du logo sur petits écrans */
            .logo-container img {
                height: 30px;
                margin-right: 5px;
            }

            header h1 {
                font-size: 20px;
            }
        }

        /* Search bar */
        .search-bar {
            display: flex;
            justify-content: center;
            margin: 20px 0;
            width: 100%;
        }

        .search-bar input {
            width: 60%;
            max-width: 600px;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 25px;
            border: 1px solid #ccc;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: width 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
        }

        .search-bar input:focus {
            outline: none;
            border-color: #005AAA;
            box-shadow: 0 4px 12px rgba(0, 90, 170, 0.3);
        }

        /* Main Section */
        .main-title {
            text-align: center;
            font-size: 28px;
            margin: 20px 10px;
            color: #005AAA;
        }

        .cards-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center; /* Centrer les cartes */
            margin: 0 20px;
            width: 100%;
            box-sizing: border-box;
        }

        .card {
            background-color: white;
            border-radius: 10px;
            width: 23%;
            min-width: 250px;
            margin: 10px 10px; /* Réduction des marges */
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .card h2 {
            font-size: 18px;
            color: #005AAA;
            margin-bottom: 10px;
        }

        .card p {
            font-size: 14px;
            margin-bottom: 15px;
            flex-grow: 1;
        }

        .cta-button {
            background-color: #005AAA;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 25px;
            font-size: 14px;
            cursor: pointer;
            transition: background-color 0.3s;
            align-self: center;
            text-decoration: none;
        }

        .cta-button:hover {
            background-color: #004080;
        }

        footer {
            background-color: #005AAA;
            color: white;
            text-align: center;
            padding: 15px 0;
            margin-top: 20px;
            width: 100%;
            box-sizing: border-box;
        }
    </style>
</head>
<body>

<header>
    <div class="logo-container">
        <img src="https://media.licdn.com/dms/image/D4E12AQGGABFQUr9H4w/article-cover_image-shrink_720_1280/0/1703173311911?e=2147483647&v=beta&t=tbVyU2VkWiYGvXYuxblen2E4y6XCycEThEV9pTwddhc"> <!-- Remplacez l'URL par celle de votre logo -->
        <h1>Impôts.gouv</h1>
    </div>
    <div class="nav-container">
        <button class="menu-btn">☰</button>
        <nav>
            <a href="#">Particulier</a>
            <a href="#">Professionnel</a>
            <a href="#">Partenaire</a>
            <a href="#">International</a>
        </nav>
        <nav class="nav-menu">
            <a href="#">Particulier</a>
            <a href="#">Professionnel</a>
            <a href="#">Partenaire</a>
            <a href="#">International</a>
        </nav>
    </div>
</header>

<div class="search-bar">
    <input type="text" placeholder="Recherchez un formulaire, une question...">
</div>

<h2 class="main-title">Informations fiscales et démarches</h2>

<div class="cards-container">
    <div class="card">
        <h2>Nouveautés fiscales</h2>
        <p>Le régime fiscal des associés de SEL évolue pour s'appliquer à partir de 2025.</p>
        <button class="cta-button">En savoir plus</button>
    </div>
    <div class="card">
        <h2>Attention aux arnaques !</h2>
        <p>Des courriels et SMS frauduleux circulent pour promettre le remboursement d'un trop perçu ou menacer de poursuites pour non paiement d'impôts ou d'amendes. Ces escroqueries n'ont pour but que de vous extorquer de l'argent ou des informations.</p>
        <button class="cta-button">En savoir plus</button>
    </div>
    <div class="card">
        <h2>Correction des déclarations</h2>
        <p>Le service de correction des déclarations de revenus en ligne est ouvert du 31 juillet 2024 au 4 décembre 2024 inclus.</p>
        <button class="cta-button">En savoir plus</button>
    </div>
    <div class="card">
        <h2>LA FACTURATION ÉLECTRONIQUE SE GÉNÉRALISE</h2>
        <p>L'État accompagnera la généralisation de la facturation électronique entre entreprises.</p>
        <button class="cta-button">En savoir plus</button>
    </div>
</div>

<footer>
    <p>© 2024 République Française - impots.gouv.fr</p>
</footer>

<script>
    // Toggle the burger menu
    document.querySelector('.menu-btn').addEventListener('click', function(event) {
        event.stopPropagation(); // Prevent the click from bubbling up to the window
        const menu = document.querySelector('.nav-menu');
        if (menu.style.display === 'flex') {
            menu.style.display = 'none';
        } else {
            menu.style.display = 'flex';
        }
    });

    // Fermer le menu lorsque l'utilisateur clique en dehors
    window.addEventListener('click', function(event) {
        const menu = document.querySelector('.nav-menu');
        const button = document.querySelector('.menu-btn');
        if (!button.contains(event.target) && !menu.contains(event.target)) {
            menu.style.display = 'none';
        }
    });
</script>

</body>
</html>
"""

# Afficher le HTML responsive via Streamlit
components.html(html_code_responsive, height=1200, scrolling=True)
