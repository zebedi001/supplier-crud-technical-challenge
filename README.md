
# Supplier CRUD Technical Challenge

A Python Flask and PostgreSQL supplier management application demonstrating CRUD operations, supplier search, responsive web design and cloud database integration.

**GitHub Repository:** https://github.com/zebedi001/supplier-crud-technical-challenge

# --------------------


## 1. What I Built and Why

### 1.1 Background — Purchase Web

Since August 2026, I have been developing *Purchase Web*, a personal financial management application, to refresh my programming knowledge and develop practical software engineering skills.

I graduated in 1995 with a BSc in Computing and Information Systems, following a two-year HND in Computing. After pursuing a career in secondary science teaching, I am now seeking to transition into software development and DevOps engineering.

Purchase Web uses Python, Flask, PostgreSQL, HTML, CSS, JavaScript and Jinja2. Its wider design includes suppliers, purchases, payments, ledgers, reporting, authentication and an AI assistant named Mara.

For the EAS technical challenge, I adapted the existing Supplier CRUD functionality into a standalone application and concentrated on three improvements.

### 1.2 The Problem I Chose to Solve

The original supplier management interface supported adding, viewing, amending and deleting suppliers, but locating a particular supplier required browsing existing records.

I implemented a search facility allowing users to enter a full or partial supplier name and retrieve matching records.

The feature demonstrates the challenge's central requirement:

**Input → Processing → Output**

- **Input:** The user enters a supplier name or part of a name.
- **Processing:** Flask passes the search term to Python, which queries PostgreSQL.
- **Output:** Jinja2 displays matching supplier records, including account, address and contact information.

### 1.3 Technical Challenge Objectives

**Priority 1 — Supplier Search: Completed**

Implemented and tested full and partial supplier-name searching, including multiple matches and input validation.

**Priority 2 — Responsive Website and Navigation: Completed for tested layouts**

Improved supplier page presentation, sidebar navigation and the eight invisible navigation hotspots surrounding the Mara spider graphic. The hotspots were tested successfully at 30%, 100% and 120% browser zoom.

**Priority 3 — Supabase Cloud PostgreSQL: Completed**

Configured the application to connect to either local PostgreSQL or Supabase-hosted PostgreSQL. Transferred demonstration supplier records and successfully tested cloud CRUD operations.

### 1.4 Technologies and Development Tools

| Technology | Purpose |
|---|---|
| Python 3.11.9 | Application logic |
| Flask | Web framework and routing |
| Jinja2 | Dynamic HTML templates |
| psycopg 3 | PostgreSQL database access |
| PostgreSQL 16 | Relational database |
| Supabase | Cloud-hosted PostgreSQL |
| HTML5, CSS3, JavaScript | Frontend and navigation |
| python-dotenv | Environment configuration |
| Git and GitHub | Version control |
| Visual Studio Code | Development environment |
| macOS Big Sur | Development operating system |

### 1.5 Scope and Design Decisions

The challenge focuses on supplier CRUD operations, supplier search, responsive navigation and cloud database access.

The original demonstration dataset contains 25 suppliers, including the fields `is_active`, `created_at` and `updated_at`.

Unfinished authentication and unrelated Purchase Web modules were excluded to keep the application focused and testable.

Local PostgreSQL and Supabase are independent databases. **Automatic synchronisation is not implemented.**

# --------------------


## 2. How to Run the Application

### 2.1 Prerequisites

Reviewers require Python 3.11 or later, Git, a web browser and the project's Python dependencies.

A local PostgreSQL installation is required only when using the local database configuration. Reviewers using Supabase instead need valid cloud database credentials and network access.

### 2.2 Downloading the Repository

Clone the GitHub repository:

`git clone https://github.com/zebedi001/supplier-crud-technical-challenge.git`

Enter the project directory:

`cd supplier-crud-technical-challenge`

Alternatively, download the repository using GitHub's **Code → Download ZIP** option.

### 2.3 Installing Python Dependencies

Create a virtual environment:

`python3 -m venv .venv`

Activate it on macOS or Linux:

`source .venv/bin/activate`

Install dependencies:

`python3 -m pip install -r requirements.txt`

The principal dependencies are Flask, psycopg 3 and python-dotenv.

**Submission check:** Confirm that `requirements.txt` exists and contains the correct packages.

### 2.4 PostgreSQL Database Configuration

The application supports two database configurations.

| Setting | Local PostgreSQL | Supabase Cloud |
|---|---|---|
| Database | `supplier_crud` | `postgres` |
| Host | `localhost` | Supabase session-pooler hostname |
| Port | Local PostgreSQL port | `5432` |
| Table | `suppliers` | `public.suppliers` |
| Connection | Local PostgreSQL | SSL required |
| Selection | `DB_MODE=local` | `DB_MODE=cloud` |

Database connection functionality is maintained in `supplierdb.py`.

### 2.5 Accessing Supabase Cloud PostgreSQL

EAS reviewers can use the cloud database without installing PostgreSQL locally, provided they have valid credentials.

**Step 1 — Obtain Cloud Credentials**

The application requires the following Supabase PostgreSQL credentials:

- `SUPABASE_HOST` — session-pooler hostname.
- `SUPABASE_USER` — PostgreSQL session-pooler username.
- `SUPABASE_PASSWORD` — database password.

The connection uses port `5432` and SSL mode `require`.

Credentials must be supplied securely by the project owner and must not be published in GitHub.

**Step 2 — Configure the Environment**

Create a file named `.env` in the project root directory.

Enter the following settings, replacing the placeholders with valid credentials:

`DB_MODE=cloud`

`SUPABASE_HOST=your-supabase-pooler-host`

`SUPABASE_USER=your-supabase-database-user`

`SUPABASE_PASSWORD=your-supabase-database-password`

Save the file. The `.env` file is excluded from GitHub using `.gitignore`.

**Step 3 — Start the Application**

Run:

`python3 App.py`

Open the local Flask address displayed in the terminal.

The application now uses Supabase PostgreSQL for supplier operations.

**Step 4 — Test the Cloud Connection**

Open **Search Supplier** and enter a full or partial supplier name.

The application should retrieve matching supplier records from Supabase.

Reviewers with suitable database permissions can also test adding, amending and deleting demonstration records.

**Important:** Supabase hosts the PostgreSQL database, not the Flask website. The Flask application runs locally.

Cloud access requires valid credentials and an accessible Supabase project. Credentials should be provided privately to authorised reviewers.

### 2.6 Using Local PostgreSQL Instead

To use the local development database, set:

`DB_MODE=local`

The application expects a local PostgreSQL database named `supplier_crud`, containing the appropriate supplier table and records.

The original demonstration dataset contains 25 suppliers.

The repository includes `suppliers_export.sql` and `suppliers_import.csv`, prepared during database migration.

Restart Flask after changing `DB_MODE`.

### 2.7 Application Navigation

The application provides the following supplier functions:

- Add Supplier
- Amend Supplier
- Delete Supplier
- Account Details
- Address Details
- Search Supplier

Navigation is available through the sidebar and Mara spider graphic.

# --------------------


## 3. How the Application Works

### 3.1 Application Architecture

The application separates frontend, backend and database responsibilities.

- **Frontend:** HTML, CSS, JavaScript and Jinja2 templates.
- **Backend:** `App.py` and supplier management Python modules.
- **Database:** `supplierdb.py` and PostgreSQL, accessed through psycopg 3.

The database connection is selected using `DB_MODE`, allowing existing supplier operations to work with either PostgreSQL environment.

### 3.2 Supplier Search — Input, Processing and Output

Supplier Search is the principal new feature developed for the technical challenge.

**Input**

The user opens `search_supplier.html` and enters a complete or partial supplier name.

The HTML form submits the search using the HTTP GET method.

**Processing**

The `/search_supplier` route in `App.py` retrieves the input using `request.args.get("name")`.

The route passes the search term to `get_search_supplier()` in `supplierdb.py`.

The function queries the selected PostgreSQL database for matching supplier names.

**Output**

Matching records are returned to Flask and rendered through Jinja2 in `search_supplier.html`.

Results include supplier identification, account details, payment terms, address, contact information, active/inactive status and creation/update timestamps.

Multiple matches are displayed separately.

An empty submitted search displays a validation message, while opening the page initially does not.

**Data Flow**

**HTML form → Flask route → Python function → PostgreSQL query → matching records → Jinja2 → browser output**

### 3.3 Supplier CRUD Operations

| Operation | Function |
|---|---|
| Create | Add a new supplier |
| Read | View supplier details or search records |
| Update | Amend an existing supplier |
| Delete | Delete a supplier record |

The existing CRUD functionality was retained from Purchase Web and tested against Supabase.

### 3.4 Supplier Database Records

Supplier records contain account, address and contact information.

Additional fields include:

- `is_active` — supplier status.
- `created_at` — creation timestamp.
- `updated_at` — last amendment timestamp.

The original local dataset contains 25 demonstration suppliers. Cloud testing may have changed the number of cloud records.

### 3.5 Responsive Website and Navigation

The application includes a fixed-width hover sidebar and invisible navigation hotspots around the Mara spider graphic.

Relevant frontend files include:

- `index_main.html`
- `index_supplier.html`
- `web_hotspots.html`
- `search_supplier.html`
- `sidebar.css`
- `web_hotspots.css`
- `sidebar_control.js`

The hotspots were repositioned to remain aligned with the spider graphic when browser zoom changes.

All eight navigation links were tested successfully at 30%, 100% and 120% zoom.

The Supplier Search page was also improved with clearer record spacing, search-field presentation and validation behaviour.

Further physical mobile-device testing remains a future improvement.

### 3.6 Supabase Cloud Integration

The original 25 demonstration supplier records were transferred to Supabase PostgreSQL.

The `supplier_database()` function selects the local or cloud connection according to `DB_MODE`.

Cloud operations were successfully tested:

- Retrieved existing supplier records.
- Amended supplier ID 5 and verified the change in Supabase.
- Confirmed the corresponding local record remained unchanged.
- Created and retrieved a test supplier.
- Deleted the test supplier and verified its removal using the Supabase SQL Editor.

These tests confirmed cloud CRUD functionality and the independence of the two databases.

### 3.7 Version Control and Documentation

Git and GitHub were used to manage development changes.

Supporting documentation includes:

- `README.md` — setup instructions and architecture.
- `RESEARCH.md` — technical investigation and problem-solving.
- `AI.md` — AI assistance and verification.

# --------------------


## 4. Testing and Verification

### 4.1 Supplier Search

Tests confirmed that full and partial supplier names returned matching records, including multiple matches.

Supplier account, address, contact and audit information was displayed.

Empty-search validation and initial page-load behaviour were corrected and tested.

### 4.2 Website Navigation

The eight Mara navigation hotspots were tested at 30%, 100% and 120% browser zoom.

Sidebar navigation and supplier page presentation were also examined.

### 4.3 Cloud PostgreSQL

Supabase connection, supplier retrieval, amendment, creation and deletion were tested successfully.

Changes were independently verified through the Supabase SQL Editor.

### 4.4 Final Submission Checks

Before submission, confirm that:

- The application starts correctly.
- Required dependencies are documented.
- Database credentials are excluded from Git.
- The GitHub repository is public.
- `README.md`, `RESEARCH.md` and `AI.md` are present.
- Cloud access instructions are accurate and reviewer credentials can be supplied securely.

# --------------------


## 5. Challenges and Lessons Learned

**Supplier Search:** Implementing the feature strengthened my understanding of HTML forms, Flask GET requests, Python functions, SQL queries and Jinja2 output.

**Search Validation:** Distinguishing an initial page visit from an empty submitted search required changes to Flask route and template logic.

**Responsive Navigation:** Correcting hotspot alignment required investigating CSS positioning and testing different browser zoom levels.

**Supabase Integration:** Configuring remote PostgreSQL required researching database connections, SSL, environment variables, credential security and data migration.

**Testing:** Independent verification through PostgreSQL and the Supabase SQL Editor helped confirm that application operations affected the intended database.

**Scope Management:** Concentrating on three defined objectives made the project achievable within the challenge deadline.

Further research and troubleshooting details are documented in `RESEARCH.md`.

# --------------------


## 6. Future Improvements

Potential developments include:

- Reintroducing authentication and role-based access control.
- Investigating controlled local-to-cloud database synchronisation.
- Hosting the Flask application for remote browser access.
- Improving mobile responsiveness and accessibility.
- Expanding input validation and database error handling.
- Introducing automated testing.
- Continuing development of Purchase Web's purchases, payments, ledgers and reporting modules.

These features were deliberately excluded from the current challenge.

# --------------------


## 7. Conclusion

The Supplier CRUD Technical Challenge builds upon an existing Python Flask application and demonstrates three completed objectives.

**Supplier Search:** Implemented full and partial supplier-name searching using Flask, Python, PostgreSQL and Jinja2.

**Responsive Web Design:** Improved supplier page presentation, sidebar navigation and Mara's eight navigation hotspots.

**Supabase Cloud PostgreSQL:** Configured cloud database access, transferred demonstration records and verified CRUD functionality.

The project demonstrates practical experience in Python development, web applications, relational databases, cloud configuration, Git, debugging, testing and technical documentation.

It also provided valuable experience in prioritising functionality, researching unfamiliar technologies and managing development within a limited timeframe.


# --------------------
