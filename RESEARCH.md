
# Supplier CRUD Technical Challenge — Research

This document summarises the technical research, problem-solving and learning undertaken during the EAS Supplier CRUD Technical Challenge.

It also provides reference websites for further study and interview preparation.

---

## 1. Supplier Search Development

### 1.1 Objective

The first priority was to implement supplier searching by full or partial name, including the first few letters.

The objective was to demonstrate:

**Input → Processing → Output**

### 1.2 HTML, CSS, JavaScript and Flask

I investigated how HTML forms submit information to Flask and how Python processes requests.

The search uses:

1. `search_supplier.html` to collect input.
2. An HTTP GET request to `/search_supplier`.
3. `App.py` to process the request.
4. `get_search_supplier()` in `supplierdb.py` to query PostgreSQL.
5. Jinja2 to display matching supplier records.

CSS controls the presentation. Existing JavaScript handles navigation; a separate search script was unnecessary.

**Research references:**

- [HTML, CSS and JavaScript — MDN](https://developer.mozilla.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Python Documentation](https://docs.python.org/3/)

### 1.3 PostgreSQL Search Queries

I investigated case-insensitive partial-name searching and returning multiple matching records.

Problems addressed included distinguishing an initial page visit from an empty search, displaying multiple matches and presenting supplier account, address, contact and audit information.

**Research:** [PostgreSQL Documentation](https://www.postgresql.org/docs/)

### 1.4 Outcome

Full and partial supplier searches were successfully tested, including multiple matches and input validation.

---

## 2. Responsive Web Design

### 2.1 Objective

The second priority was improving the sidebar, supplier page presentation and eight invisible navigation hotspots surrounding the Mara spider graphic.

### 2.2 CSS and JavaScript Research

I investigated CSS positioning, fixed-width layouts, Grid units, hover behaviour and browser zoom.

Relevant files included:

- `index_main.html`
- `index_supplier.html`
- `web_hotspots.html`
- `web_hotspots.css`
- `sidebar.css`
- `sidebar_control.js`

JavaScript controls the sidebar's hover behaviour.

The main challenge was maintaining hotspot alignment as browser zoom changed.

**Research references:**

- [CSS Positioning — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/position)
- [CSS Grid — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout)
- [Responsive Design — MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design)

### 2.3 Outcome

All eight Mara hotspots were successfully tested at 30%, 100% and 120% browser zoom.

Further mobile-device testing remains a future improvement.

---

## 3. Cloud PostgreSQL — Supabase and Neon

### 3.1 Cloud Provider Research

I investigated Supabase and Neon as potential PostgreSQL cloud-hosting services.

Research included PostgreSQL compatibility, database connections, SSL, credentials, connection pooling and importing records.

Supabase was selected for implementation.

**Research references:**

- [Supabase Documentation](https://supabase.com/docs)
- [Supabase Database Connections](https://supabase.com/docs/guides/database/connecting-to-postgres)
- [Neon Documentation](https://neon.com/docs)

### 3.2 PostgreSQL Tables and Migration

The local application uses PostgreSQL 16 and the `supplier_crud` database.

Supabase uses the `postgres` database with the `public.suppliers` table.

The 25 demonstration supplier records were transferred to Supabase.

I investigated SQL table creation, data types, primary keys, CSV imports and SQL exports.

Important fields include `id`, `is_active`, `created_at` and `updated_at`.

**Research references:**

- [PostgreSQL — CREATE TABLE](https://www.postgresql.org/docs/current/sql-createtable.html)
- [PostgreSQL — COPY](https://www.postgresql.org/docs/current/sql-copy.html)
- [Supabase — Importing Data](https://supabase.com/docs/guides/database/import-data)

### 3.3 Python Database Configuration

The `supplier_database()` function in `supplierdb.py` selects the database using:

- `DB_MODE=local` — local PostgreSQL.
- `DB_MODE=cloud` — Supabase PostgreSQL.

I investigated `psycopg`, environment variables, SSL and Supabase session-pooler connections using port 5432.

Credentials are stored in `.env`, which is excluded from GitHub.

**Research references:**

- [psycopg 3 Documentation](https://www.psycopg.org/psycopg3/docs/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### 3.4 Testing and Outcome

Cloud testing successfully verified:

1. Retrieving supplier records.
2. Amending supplier ID 5.
3. Adding and retrieving a test supplier.
4. Deleting the test supplier.
5. Checking changes through the Supabase SQL Editor.

Local and cloud databases remain independent. Automatic synchronisation was not implemented.

---

## 4. Development Tools — Bash and GitHub

### 4.1 macOS Bash Commands

I investigated terminal commands for running Flask, accessing PostgreSQL and resolving port conflicts.

| Command | Purpose |
|---|---|
| `python3 App.py` | Start Flask |
| `source .venv/bin/activate` | Activate Python environment |
| `python3 -m pip install -r requirements.txt` | Install dependencies |
| `lsof -nP -iTCP:5004 -sTCP:LISTEN` | Identify a process using port 5004 |
| `kill PID` | Terminate a selected process |
| `/Library/PostgreSQL/16/bin/psql` | Access PostgreSQL |

**Research references:**

- [GNU Bash Manual](https://www.gnu.org/software/bash/manual/)
- [PostgreSQL — psql](https://www.postgresql.org/docs/current/app-psql.html)

### 4.2 Git and GitHub

A separate repository was created for the challenge.

I investigated Git commands for checking changes, recording commits and pushing updates.

| Command | Purpose |
|---|---|
| `git status` | Check changes |
| `git add .` | Stage files |
| `git commit -m "message"` | Record changes |
| `git push` | Upload commits |
| `git remote -v` | Check remote repository |
| `git ls-files` | List tracked files |

**Research references:**

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Documentation](https://docs.github.com/)
- [Visual Studio Code Documentation](https://code.visualstudio.com/docs)

---

## 5. ChatGPT — AI-Assisted Learning and Development

### 5.1 How I Used ChatGPT

I have a ChatGPT Plus subscription, which I use as a learning, research and development resource while refreshing my programming knowledge and becoming familiar with modern technologies.

Having originally studied Computing in the 1990s, I have been relearning programming and developing my practical coding skills.

My preferred approach is to work through problems step by step, often examining code line by line to understand what each instruction does.

When I encounter difficulties, I use ChatGPT to investigate problems, explain unfamiliar concepts, find relevant documentation and assist with coding and debugging when necessary.

### 5.2 Questioning AI Responses

I do not automatically accept ChatGPT's recommendations.

I regularly ask follow-up questions, challenge explanations, request further investigation and reject suggestions that appear incorrect, unnecessary or overly complicated.

I also verify suggested solutions by reviewing code, running the application, testing functionality and checking database results.

My objective is to understand the underlying programming concepts rather than simply obtain working code.

### 5.3 AI-Assisted Documentation

I also used ChatGPT to help formulate and structure `README.md`, `RESEARCH.md` and `AI.md`.

I supplied the project information, explained the work undertaken and directed how the documents should be organised.

ChatGPT assisted with drafting and formatting the Markdown content.

I reviewed the material, questioned statements, requested amendments and checked that it accurately reflected the implemented application.

### 5.4 Outcome

ChatGPT has been a useful interactive learning, research and debugging resource.

I remain responsible for development decisions, reviewing suggested solutions and verifying the resulting application.

**AI tool:** [OpenAI ChatGPT](https://chatgpt.com/)

**Further details:** See `AI.md` for AI assistance, corrections and verification.

---

## 6. Lessons Learned and Future Research

### 6.1 Technical Learning

This challenge strengthened my understanding of:

- HTML forms, Flask routes and HTTP GET requests.
- Python functions and PostgreSQL queries.
- Jinja2 templates and dynamic output.
- CSS positioning and responsive navigation.
- Cloud database connections and migration.
- Environment variables and credential security.
- Bash troubleshooting and Git version control.
- Critically evaluating AI-generated suggestions.

### 6.2 Future Improvements

Potential developments include automated testing, improved mobile responsiveness, stronger validation, authentication, remote application hosting and controlled local-to-cloud database synchronisation.

---

## 7. Research Websites and Interview Preparation

The following websites provide reference material for reviewing the technologies used in the challenge. They are not all claimed as sources personally consulted during development.

| Subject | Website |
|---|---|
| Python | [docs.python.org](https://docs.python.org/3/) |
| Flask | [flask.palletsprojects.com](https://flask.palletsprojects.com/) |
| Jinja2 | [jinja.palletsprojects.com](https://jinja.palletsprojects.com/) |
| HTML, CSS, JavaScript | [developer.mozilla.org](https://developer.mozilla.org/) |
| PostgreSQL | [postgresql.org/docs](https://www.postgresql.org/docs/) |
| psycopg | [psycopg.org](https://www.psycopg.org/psycopg3/docs/) |
| Supabase | [supabase.com/docs](https://supabase.com/docs) |
| Neon | [neon.com/docs](https://neon.com/docs) |
| Bash | [GNU Bash Manual](https://www.gnu.org/software/bash/manual/) |
| Git | [git-scm.com/doc](https://git-scm.com/doc) |
| GitHub | [docs.github.com](https://docs.github.com/) |
| VS Code | [code.visualstudio.com/docs](https://code.visualstudio.com/docs) |
| ChatGPT | [chatgpt.com](https://chatgpt.com/) |

---

## 8. Conclusion

The technical challenge provided practical experience in researching, developing and testing functionality across Python, Flask, PostgreSQL, web design and cloud infrastructure.

The three main outcomes were supplier searching, improved responsive navigation and successfully tested Supabase PostgreSQL integration.

The research also reinforced the importance of debugging, questioning technical advice, verifying results and managing development priorities within a limited timeframe.
