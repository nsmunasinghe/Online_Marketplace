# Online Marketplace 🛒

Welcome to the Online Marketplace project! This repository contains the codebase for a web-based marketplace application built using Python, Django, and SQLite3.

## 📌 Table of Contents

  - [📌 Project Overview](#-project-overview)
  - [📌 Features](#-features)
  - [📌 Technologies Used](#-technologies-used)
  - [📌 Setup and Installation](#-setup-and-installation)
  - [📌 Usage](#-usage)
  - [📌 Contributing](#-contributing)
  - [📌 License](#-license)

## 📌 Project Overview

The Online Marketplace project is a web application that allows users to buy and sell products. It provides a platform where users can register, list items for sale, browse items from other sellers, and make purchases. The project aims to simulate a real-world e-commerce environment with essential functionalities.

## 📌 Features

- User Authentication (Sign Up, Login, Logout)
- Product Listing and Browsing
- Product Search
- Shopping Cart
- Order Management
- User Profile Management

## 📌 Technologies Used

- **Python**: The core programming language used for development.
- **Django**: The web framework used to build the application.
- **SQLite3**: The database system used for data storage.

## 📌 Setup and Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
    ```powershell
    git clone https://github.com/nsmunasinghe/Online_Marketplace.git
    ```
    ```powershell
    cd Online_Marketplace
    ```

2. **Create a virtual environment:**

    ```powershell
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    ```powershell
    .\venv\Scripts\Activate.ps1
    ```

4. **Install the dependencies:**

    ```powershell
    pip install -r requirements.txt
    ```

5. **Apply migrations:**

    ```powershell
    python manage.py migrate
    ```

6. **Create a superuser (admin):**

    ```powershell
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```powershell
    python manage.py runserver
    ```

8. **Access the application:**
    Open your browser and go to `http://127.0.0.1:8000/`

## 📌 Usage

- **Home Page:** View the homepage with featured products and categories.
- **Sign Up / Login:** Register a new account or log in with existing credentials.
- **Product Listing:** Add new products to sell.
- **Product Browsing:** Browse available products and use the search functionality.
- **Shopping Cart:** Add products to the cart and proceed to checkout.
- **Order Management:** View your orders and order history.
- **User Profile:** Manage your profile details and view your listings.

## 📌 Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a Pull Request.

## 📌 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance!

