import streamlit as st
import streamlit.components.v1 as components

# Ton code HTML complet
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
        }

        /* Header styling */
        header {
            background-color: #005AAA;
            color: white;
            padding: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        header h1 {
            font-size: 20px;
        }

        /* Navigation styling */
        nav {
            display: flex;
            justify-content: space-around;
            margin: 15px 0;
            list-style-type: none;
        }

        nav a {
            text-decoration: none;
            color: #005AAA;
            font-size: 16px;
            font-weight: bold;
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
            top: 50px;
            right: 10px;
            background-color: #005AAA;
            border-radius: 5px;
            padding: 10px;
        }

        .nav-menu a {
            color: white;
            margin: 10px 0;
            font-size: 16px;
        }

        /* Responsive styles for small screens */
        @media (max-width: 768px) {
            .menu-btn {
                display: block;
            }

            nav {
                display: none;
            }

            .nav-menu {
                display: flex;
                right: 0;
            }
        }

        /* Search bar */
        .search-bar {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }

        .search-bar input {
            width: 60%;
            padding: 12px;
            font-size: 16px;
            border-radius: 25px;
            border: 1px solid #ccc;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Main Section */
        .main-title {
            text-align: center;
            font-size: 28px;
            margin: 20px 0;
            color: #005AAA;
        }

        .cards-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            margin: 0 10px;
        }

        .card {
            background-color: white;
            border-radius: 10px;
            width: 30%;
            margin: 20px 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .cta-button {
            background-color: #005AAA;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
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
    <a href="#">Particulier</a>
    <a href="#">Professionnel</a>
    <a href="#">Partenaire</a>
    <a href="#">International</a>
</nav>

<!-- Large screen menu -->
<nav>
    <a href="#">Particulier</a>
    <a href="#">Professionnel</a>
    <a href="#">Partenaire</a>
    <a href="#">International</a>
</nav>

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

# Afficher le HTML responsive via Streamlit
components.html(html_code_responsive, height=800)
