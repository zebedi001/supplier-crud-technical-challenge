# supplier-crud-technical-challenge
A Python Flask and PostgreSQL supplier management application demonstrating CRUD operations and local-to-cloud database synchronisation.

# -------------------------
What you built and why?

Since late August 2026 after work, I have been working on a Purchase Ledger financial system called Purchase Web.  This is a personal project in order to re-learn various modern and old coding languages, and development tools. It is a basic stack configuration containing suppliers, purchases, payments, ledger, reports, settings, and an AI Assistant called Mara. I have nearly completed the full architecure in terms of connections through Flask backend and frontend.  The Supplier section is fully working in a basic fashion with CRUD operations which originally wrote to SQLite3, but now transitioned to using PostgreSQL. The basic stack currently utilises: Python | Flask | PostgreSQL | HTML | CSS | Jinja2 | JavaScript, using DevOps Visual Code | GitHub | Bash.

For this technical challenge I have decided to utilise the Supplier section and improve upon it.  Given the deadline and time I have, I will try and incorporate an online Cloud storage. In essence when a supplier is added, amended or deleted, the database in the cloud is also updated. I intend to try and use synchronisation to ensure the update even if a connection is not available, and queued for update later.  
