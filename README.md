# supplier-crud-technical-challenge
A Python Flask and PostgreSQL supplier management application demonstrating CRUD operations and local-to-cloud database synchronisation.

# -----------------------
# What you built and why?
#------------------------

Since late August 2026 after work, I have been working on a Purchase Ledger financial system called Purchase Web.  This is a personal project in order to re-learn various modern and old coding languages (graduated with my Computing degree in 1995), and utilising development tools. It is a basic stack configuration containing suppliers, purchases, payments, ledger, reports, settings, and an AI Assistant called Mara to assist in reporting via NLP.  I have nearly completed the full architecture in terms of connections through Flask backend and frontend.  The Supplier section is fully working in a basic fashion with CRUD operations which originally wrote to SQLite3, but now transitioned to using PostgreSQL. The basic stack currently utilises: Python | Flask | PostgreSQL | HTML | CSS | Jinja2 | JavaScript, using DevOps Visual Code | GitHub | Bash. I have duplicated my Purchase_Ledger folder and called it supplier-crud-technical-challenge, and have hashed out the Authorisation.py related code I was working on in App.py and other files that may be applicable to get suppliers ready for the challenge.

For this Technical Challenge I have decided to utilise the Supplier section and improve upon it.  Given the deadline and time I have I will try to:
  1. I have two options in Suppliers where a user can view a list of supplier accounts (25 records pre challenge) and supplier addresses. I will          improve on this list in terms of presentation, and add a new option to search on a supplier name from the database of 5-10 more records              that I will add, amend several and delete several. I will test the code and show screenshots of the results.

  2. To improve the output by making it more responsive, no matter the type of technology used - Responsive Web Design (RWD). These improvements          will be to the sidebar and main container screens. I hope to make the sidebar open or closed when the mouse is moved to the left of the screen,      and have a button that allows a user to click a box and keep the sidebar in view. I use two methods to navigate around Purchase Web. The             sidebar and a spider web ends at West, North Nest, North, North East, East, South, and two links at the centre, one for returning to the             main menu and the other a link to Mara AI Assistant. These links are currently out of position, and do not stay in position when                     zooming in and out, or for different screens, such as iPads and mobiles. I intend to make sure they are fixed.

Improvements for the future:
  I did think about implementing a Cloud storage for the challenge, but having re-read the email it specifically asked for inputing code and
  outputing that code in a presentable way for users. However, I have already set up and installed 'Superbase' app cloud storage and authorised it
  on GitHub for supplier-crud-technical-challenge repository. The code will ensure synchronisation between the database on the MacOs and in the 
  cloud. If there isn't a current connection the update will be queued until reconnected.
  
