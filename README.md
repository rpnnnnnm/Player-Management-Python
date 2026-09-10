🖥️ Sistem Informasi Rental PlayStation (Java)
A desktop-based PlayStation rental management application developed using Java (NetBeans IDE) and MySQL for database integration. This system is designed to streamline rental operations, customer management, and transaction tracking.

📌 Project Overview
This application manages the daily operations of a PlayStation rental business. It features a structured Java NetBeans project architecture (utilizing controllers, models, views, and database helper classes) supported by a MySQL database to securely handle unit inventories, customer records, and payment logs.

✨ Key Features
Authentication & Login: Secure login system (LoginFrame, AuthController) for operators to access the application dashboard.

Console Management: Monitor and manage various PlayStation unit generations (PS3, PS4, and PS5) and their active statuses.

Customer Management (Pelanggan): Register, track, and manage customer details (PelangganFrame).

Rental Transactions: Handle active rental logs, duration tracking, and automated calculation of rental bills.

Payment Processing: Support flexible payment methods including both Cash (PembayaranCash) and Bank Transfer (PembayaranTransfer) options.

🛠️ Tech Stack & Architecture
Programming Language: Java

IDE: NetBeans

Database: MySQL (database.sql)

Database Connector: MySQL JDBC Driver (mysql-connector-java)

Architecture Pattern: MVC-style separation (Controllers, Models, Views, and Utilities/Exceptions)

🚀 How to Run
Clone or download this repository.

Import the provided database.sql file into your local MySQL server.

Open the project directory inside NetBeans IDE.

Adjust the database connection settings inside the Koneksi.java or DatabaseHelper.java file if your local database credentials require it.

Run the project from Main.java or launch the initial login frame.

👥 Team Members (Group 5 - IF-8)
Yusuf Rizqi Aulia (10125359)

Fakhri Sofyan (10125326)

Sandy Dwi Cahyo Nugroho (10125330)

Hiqmal Fajryan Anwar (10125339)

Rangga Syatir Heriza (10125308)

Ripan Maulana Suhur (10125318)
