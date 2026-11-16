# supplier-crud-technical-challenge
A Python Flask and PostgreSQL supplier management application demonstrating CRUD operations and local-to-cloud database synchronisation.


1. What I Built and Why
1.1 Background — Purchase Web
Since late August 2026, I have been developing a personal financial management application called Purchase Web, working on the project outside my normal employment as a secondary school science teacher.

I graduated in 1995 with a BSc in Computing and Information Systems, following a two-year HND in Computing. Having subsequently pursued a career in education, I am now seeking to transition from teaching into software development and DevOps engineering.

I started Purchase Web to refresh my programming knowledge, revisit previously learned languages and gain practical experience with modern software development technologies, tools and engineering practices. The project also provides an opportunity to demonstrate my commitment to learning and developing the technical skills required for a new career.

The wider Purchase Web application is designed to manage suppliers, purchases, payments, ledgers and financial reports. It also includes plans for application settings, user authentication and an AI assistant named Mara, intended to support natural-language queries and reporting.

The application uses a Python Flask backend with HTML, CSS, JavaScript and Jinja2 templates for its frontend. Supplier data was originally stored in SQLite3 before being migrated to PostgreSQL.

At the start of the EAS technical challenge, the Supplier section already supported basic Create, Read, Update and Delete (CRUD) operations. I therefore chose to use this existing functionality as the foundation for a smaller, standalone application that I could improve, test and explain within the challenge deadline.

As the main improvement, and to demonstrate the challenge's input, processing and output requirements, I designed and implemented a supplier search option. This will allow a user to enter a full or partial supplier name, search the PostgreSQL database and display matching supplier records. The user can then select a supplier to view its details.
----------------------------------------
1.2 The Problem I Chose to Solve
The existing Supplier section of Purchase Web allows users to view supplier account and address records, as well as add, amend and delete supplier information. However, finding a particular supplier requires the user to browse through the available records.

Although the demonstration database contains only 25 suppliers, manually searching through a list would become increasingly inefficient as the number of suppliers grows.

To address this problem, I decided to introduce a supplier search facility that allows users to find suppliers by entering a full or partial supplier name.

This improvement demonstrates the three main requirements of the EAS technical challenge:
1. Input: The user enters a supplier name or the first few characters of a name into a search field.
2. Processing: The Flask application receives the search request and queries the PostgreSQL database for matching supplier records.
3. Output: The application displays a list of matching suppliers. The user can then select a supplier to view its details, including account and address information.
The objective is to provide a straightforward, useful feature that improves the user experience while demonstrating how Python, Flask, PostgreSQL and Jinja2 work together to process user input and present meaningful results.
Database Architecture and Future Development
During initial development, the application used a local PostgreSQL database on my Mac. However, as Purchase Web is intended to become a downloadable application in the future, I have decided that a cloud-hosted PostgreSQL database would be a more appropriate long-term solution.

A centralised cloud database would allow authorised users to access the same supplier records from different computers without needing to install and maintain a separate PostgreSQL database on each device.

For the EAS technical challenge, I successfully connected the Flask application to a PostgreSQL database hosted by Supabase. The application can now select either the local or cloud database through the DB_MODE environment setting, without rewriting the supplier search or CRUD functionality.

This provides an option for EAS reviewers to test the application using the cloud database, provided suitable configuration and securely supplied database credentials are available.

The local PostgreSQL database has been retained for development and as an alternative configuration. The two databases are independent: selecting one does not update the other. Automatic synchronisation is not part of this implementation and may be considered as a future improvement.

This approach allows me to demonstrate the core input, processing and output requirements while exploring a database architecture that could support the future development of Purchase Web.
----------------------------------------
1.3 Technical Challenge Objectives and Priorities
After reviewing the EAS technical challenge requirements, I decided to concentrate on improving the existing Supplier section of Purchase Web rather than attempting to develop an entirely new application within the available time.

I established three development priorities, ordered according to their importance to the challenge.
Priority 1 — Supplier Search: Input, Processing and Output
My primary objective was to design and implement a supplier search facility using Python, Flask and PostgreSQL.

The user enters a full or partial supplier name, the application searches the database for matching records, and the results are displayed in a selectable list. Selecting a supplier displays its details.

This directly addresses the three core requirements of the EAS challenge: accepting input, processing that input and producing useful output.
Priority 2 — Responsive Web Design and Navigation
My second priority was to improve the presentation and usability of the existing application.

This includes improving the layout of the supplier pages, making the interface more responsive to different screen sizes and browser zoom levels, and refining the sidebar navigation.

I also intend to improve the positioning of the invisible navigation hotspots surrounding the Purchase Web spider graphic, so they remain aligned with their intended locations.

These improvements are intended to make the application easier to navigate and provide a more consistent experience across desktop, tablet and mobile screens.
Priority 3 — Cloud Database Configuration
My third priority was to investigate using Supabase to host a PostgreSQL database in the cloud. This objective was completed successfully.

The Flask application now connects to either the local PostgreSQL database or the cloud-hosted database, according to its environment configuration, without changing the supplier search and CRUD functionality.

The local database remains available for development, while the cloud database provides an additional option for future deployment and reviewer testing.

Cloud integration was an optional extension, undertaken after the core supplier search functionality was working. The connection and cloud CRUD operations have now been tested successfully.
Managing Scope and Time
I deliberately prioritised a smaller, functional application that I could explain and test rather than introducing unnecessary complexity.

This approach reflects the EAS guidance that technical understanding, research, problem-solving and sensible engineering decisions are more important than the overall size of the project.
----------------------------------------
1.4 Technologies and Development Tools
The Supplier CRUD Technical Challenge uses a combination of backend, frontend, database and development technologies. These were selected to support the existing Purchase Web architecture while providing opportunities to develop my technical knowledge and practical programming skills.
Backend Technologies
- Python 3.11.9: The main programming language used to implement application logic, supplier operations and database interactions.
- Flask: A lightweight Python web framework used to handle HTTP requests, define application routes and connect the frontend to backend functionality.
- Jinja2: Flask's templating engine, used to dynamically generate HTML pages and display supplier information returned from the database.
- psycopg: A PostgreSQL database adapter used to execute SQL queries and retrieve supplier records.
Frontend Technologies
- HTML5: Provides the structure of the application's pages, forms and navigation.
- CSS3: Controls the visual appearance, layout and responsive behaviour of the application.
- JavaScript: Provides client-side interactions, including sidebar behaviour and navigation functionality.
Database Technologies
- PostgreSQL 16: The relational database management system used to store supplier account and address information.
- SQLite3: The database system originally used during the early development of Purchase Web before migration to PostgreSQL.
- Supabase: A cloud platform providing hosted PostgreSQL, now configured and tested as an alternative database for the Flask application.
Development and Version Control Tools
- Visual Studio Code: The main development environment used to write, edit and debug the application.
- Git: Used to track changes to the source code and maintain a development history.
- GitHub: Hosts the project repository and provides access to the source code and documentation for EAS reviewers.
- Bash / macOS Terminal: Used to run Python scripts, execute PostgreSQL commands, manage files and perform Git operations.
- python-dotenv: Used to load environment variables from a local .env file, allowing configuration values and database credentials to be kept separate from the application source code.
Development Environment
The application has been developed on a MacBook Air running macOS Big Sur 11.7.11, using Python 3.11.9 and PostgreSQL 16.

The project uses a Flask-based web architecture, separating the application's Python backend, HTML templates, CSS stylesheets, JavaScript files and PostgreSQL database interactions.

This separation helps make the application easier to understand, maintain, test and extend.
----------------------------------------
1.5 Scope and Design Decisions
For the EAS technical challenge, I decided to develop a standalone Supplier CRUD application based on the existing Supplier section of Purchase Web, rather than build an entirely new application from scratch.

This decision allowed me to concentrate on developing new functionality, improving the user interface and investigating cloud database integration while working within the available time.
Application Scope
The application focuses on supplier management and includes:
- Creating new supplier records.
- Viewing supplier account and address information.
- Amending existing supplier records.
- Deleting supplier records.
- Searching for suppliers using full or partial names.
- Displaying matching search results and allowing the user to select an individual supplier.
- Displaying supplier account and address details, including active/inactive status (is_active), record creation date (created_at) and last amendment date (updated_at) when a supplier is selected from the search results.
The demonstration database contains 25 supplier records, providing a manageable dataset for testing and reviewing the application.
Design Decisions
1. Reusing the existing application architecture

I retained the Python Flask backend, PostgreSQL database and existing HTML, CSS, JavaScript and Jinja2 components. This avoided unnecessary redevelopment and allowed me to focus on improving the existing application.

2. Separating application functionality

Supplier operations are organised into separate Python modules, with Flask routes connecting the frontend to the database functionality. This makes the code easier to understand, maintain and extend.

3. Removing authentication from the challenge application

The original Purchase Web project includes authentication and user authorisation functionality under development. I temporarily disabled this functionality in the standalone technical challenge to avoid introducing unfinished features and unnecessary complexity.

Authentication and role-based access control remain planned improvements for the wider Purchase Web application.

4. Retaining supplier information and audit fields

The PostgreSQL supplier records retain their account and address information, active/inactive status (is_active), creation date (created_at) and last-updated date (updated_at).

These fields support supplier record management and provide a foundation for future auditing and reporting functionality.

5. Configuring local and cloud database connections

I retained local PostgreSQL for development and configured Supabase as a cloud-hosted alternative.

The implemented architecture allows the application to select its database connection through the DB_MODE setting in .env, without requiring changes to the supplier search or CRUD operations.

This supports testing in different environments and provides a foundation for future deployment. It does not automatically synchronise the two databases.

6. Limiting additional functionality

The wider Purchase Web application is intended to include modules for Purchases, Payments, Ledgers, Reports, Settings and the Mara AI Assistant. These modules have not yet been fully developed and remain planned future improvements to Purchase Web.

I deliberately excluded these unfinished modules from the standalone EAS technical challenge so that I could concentrate on the existing Supplier functionality, implement the new supplier search feature and improve the application's usability.

I also decided not to implement automatic database synchronisation at this stage, as it would introduce additional complexity beyond the main challenge requirements.
Overall Approach
My objective was to produce a manageable, functional application that demonstrates practical programming skills, technical understanding, problem-solving and sensible engineering decisions.

By limiting the scope, I could concentrate on implementing and explaining the supplier search functionality, improving the user experience and researching technologies that could support future development.
----------------------------------------
2. How to Run the Application
2.1 Prerequisites and Software Requirements
The Supplier CRUD Technical Challenge is a Python Flask web application that uses PostgreSQL to store and retrieve supplier information.

Before running the application locally, the following software is required:
- Python 3.11 or later: Used to run the Flask application and its backend modules. The application was developed using Python 3.11.9.
- PostgreSQL 16: The relational database management system used to store supplier records. The application was developed and tested using PostgreSQL 16.
- Git: Used to clone the project repository from GitHub.
- A web browser: Such as Firefox, Chrome or Safari, to access the application's web interface.
The application also requires several Python packages, including Flask, psycopg and python-dotenv. Installation of these dependencies is covered in Section 2.4.
Development Environment
The application was developed using Visual Studio Code on a MacBook Air running macOS Big Sur 11.7.11.

Although developed on macOS, Flask and PostgreSQL are cross-platform technologies and can also be used on Windows and Linux, subject to the appropriate software installation and configuration.
Database Requirement
The application requires access to a PostgreSQL database containing the supplier table and its associated records.

The development database is named supplier_crud and contains 25 demonstration supplier records.

Instructions for configuring the database connection are provided in Section 2.3.
----------------------------------------
2.2 Accessing the GitHub Repository
The Supplier CRUD Technical Challenge source code and supporting documentation are hosted in a GitHub repository.

GitHub Repository:

https://github.com/zebedi001/supplier-crud-technical-challenge

EAS reviewers can access the public repository directly through the link above to examine the application's source code, project structure, documentation and Git commit history.

The repository includes:
- README.md: Explains what I built and why, how to run the application, how it works and potential future improvements.
- RESEARCH.md: Documents technical research, problem-solving, resources consulted and lessons learned.
- Python source files: Contain the Flask application, supplier operations and PostgreSQL database interactions.
- HTML, CSS and JavaScript files: Provide the application's user interface, navigation and presentation.
Cloning the Repository

Reviewers who wish to download and run the application locally can open a terminal and enter:

git clone https://github.com/zebedi001/supplier-crud-technical-challenge.git

Then navigate into the project directory:

cd supplier-crud-technical-challenge

Alternatively, the source code can be downloaded using GitHub's Code → Download ZIP option.

The application requires Python dependencies and a configured PostgreSQL database before it can be executed. These requirements are explained in the following sections.

Sensitive configuration information, including database passwords, must not be committed to the public repository.
----------------------------------------
2.3 PostgreSQL Database Configuration
The Supplier CRUD Technical Challenge uses PostgreSQL as its relational database management system to store, retrieve and manage supplier information.

The application was initially developed using a locally installed PostgreSQL 16 database. I have since successfully configured a Supabase-hosted PostgreSQL database and verified that the Flask application can read and modify supplier records in the cloud.

Local Database Configuration

The existing development database is configured as follows:
- Database system: PostgreSQL 16
- Database name: supplier_crud
- Database host: localhost
- Database user: postgres
- Database connection module: supplierdb.py
- Python database adapter: psycopg (version 3)
The local database contains 25 demonstration supplier records used to test the application's search and CRUD functionality.

Each supplier record contains account and address information, active/inactive status (is_active), creation timestamp (created_at) and last-updated timestamp (updated_at).

Database Connection and Application Architecture

The application uses the Python psycopg library to establish a connection between the Flask backend and PostgreSQL.

Database connection functionality is maintained in supplierdb.py, allowing the supplier management modules to interact with the database.

The application can connect to either local PostgreSQL or Supabase-hosted PostgreSQL using environment-based configuration. In supplierdb.py, the supplier_database() function checks DB_MODE: cloud selects the Supabase connection, while local selects the local database.

This approach allows the existing supplier search and CRUD operations to work with the selected database without requiring changes to the application interface. It is a choice of connection, not a simultaneous connection or automatic synchronisation.

Supabase Cloud Database Integration

Supabase provides a cloud-hosted PostgreSQL database that can be accessed remotely through a secure database connection.

I created a Supabase project and transferred the original 25 demonstration supplier records from local PostgreSQL to the cloud database. The database table is public.suppliers; the cloud database name is postgres.

The Flask application can now retrieve and modify supplier records in Supabase. Reviewers using the cloud configuration do not need to install a local PostgreSQL server, but they do need the Python application, its dependencies, network access and valid database credentials.

The cloud connection and transfer were completed and verified. A direct database query returned 25 supplier records. I then used the Flask interface to amend supplier ID 5 and independently confirmed the change in Supabase while the local database remained unchanged. I also created a test supplier (ID 27), retrieved it, deleted it through Flask and verified in the Supabase SQL Editor that the deleted record no longer existed. These tests confirmed Create, Read, Update and Delete operations against the cloud database.

Automatic synchronisation between local PostgreSQL and Supabase is not included in the current implementation.

Database Security and Environment Variables

Database connection credentials must be kept separate from the application's source code and must not be committed to the public GitHub repository.

The project uses .gitignore to exclude local environment files, including .env.

The python-dotenv package loads environment variables from .env to configure local and cloud database connections. The implemented variables are DB_MODE, SUPABASE_HOST, SUPABASE_USER and SUPABASE_PASSWORD; local connection settings are retained separately. Supabase connections use the PostgreSQL session pooler on port 5432 with sslmode="require".

Cloud database access requires suitable credentials and permissions. These must be provided securely rather than embedded in publicly accessible source code. In particular, the Supabase database password must not be placed in the README, sample configuration, Git history or public repository.

Reviewer Access and Testing

My intended approach is to make the application straightforward for EAS reviewers to download, run and test.

The application has been configured and tested against a Supabase-hosted PostgreSQL database initially populated with 25 demonstration supplier records.

Reviewers with securely provided cloud database credentials can run the Flask application locally and retrieve supplier records directly from Supabase without installing PostgreSQL or manually creating the demonstration dataset. The Flask web server itself is not hosted on Supabase.

Reviewers will still need Python and the required application dependencies, together with an appropriately configured and secure method of accessing the cloud database. Cloud access is not publicly enabled simply because the GitHub repository is public.

Local PostgreSQL will remain available as an alternative development and testing environment.

This approach is intended to reduce the setup required for reviewers while demonstrating the use of both local and cloud-hosted relational databases.

Selecting the Database

The database selection is made in the local .env file:
- Set DB_MODE=local to use the local PostgreSQL database (supplier_crud on localhost).
- Set DB_MODE=cloud to use the Supabase-hosted PostgreSQL database. This requires SUPABASE_HOST, SUPABASE_USER and SUPABASE_PASSWORD to be configured with valid credentials.
- Restart the Flask application after changing DB_MODE, because the setting is loaded when the application starts.
The database credentials are not supplied in the public repository. The cloud connection is intended for authorised testing only; it should not use publicly shared administrative credentials.

Demonstration Data and Migration Files

The repository includes suppliers_export.sql and suppliers_import.csv, generated during preparation and transfer of the original 25 demonstration supplier records. These files document the migration process and may assist with preparing a local test database, subject to the table structure and import instructions. Subsequent cloud CRUD tests created additional records, so the current cloud dataset should not be assumed to contain exactly 25 rows.




# ----------------------------------------







# ----------------------------------------






# ----------------------------------------








# ----------------------------------------