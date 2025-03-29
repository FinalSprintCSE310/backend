# Overview
Our goal with this project was to combine our skills in frameworks, JavaScript, HTML, CSS, databases, and APIs to create a cohesive and useful product.
 
We designed a school management system (SMS) to allow organizations, teachers, students, and parents to manage school operations in one software. It provides features such recordkeeping, class management, and communication.
 
Our purpose in creating this software was to design something with real-world value and to make a powerful addition to our software portfolios.
 
# Development Environment
The tools/technologies that we used to build this product are:
1. Python
    1. FastAPI
    2. postgres connection: psycopg2
2. JavaScript
    1. VueJS
    2. TailwindCSS
3. SQL
    1. PostgreSQL
4. Netlify (Frontend Hosting)
5. Render or VPS(Backend Hosting)
 
# Useful Websites
- [FastAPI](https://fastapi.tiangolo.com/learn/)
- [VueJS](https://vuejs.org/guide/introduction.html)
- [TailwindCSS](https://tailwindcss.com/docs/installation/using-vite)
 
# Future Work
 
{Make a list of things that you need to fix, improve, and add in the future.}
 
- Add Other logins
- Add Ability to authorize users from Organization side
- Add functionality to add Class and messaging


# Cantva Backend
After cloning this repository please make sure you are creating a new branch based on the feature you will be working on. After you are done with creating a branch, please run this command in your terminal to install all the dependencies `pip install -r requirements.txt`.

After the dependencies are install you can run the server by using this command: `uvicorn main:Server --reload` this is for development mode only, we won't be using this command in production environment.