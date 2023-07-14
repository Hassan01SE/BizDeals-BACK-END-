<h1>BizDeals Backend</h1>

<p>BizDeals backend is built using Django and Django REST Framework. It serves as the server-side implementation for the BizDeals marketplace, providing API endpoints and handling business logic.</p>

<h2>Project Overview</h2>

<p>BizDeals is a comprehensive marketplace designed to facilitate the buying and selling of businesses and digital products. Built with Django and Django REST Framework, the backend handles user authentication, business listing management, secure payment processing using Stripe, and more. The project follows a C2C model where sellers can list their businesses for potential buyers.</p>

<a href="https://imgbb.com/"><img src="https://i.ibb.co/W3gK9rp/Picture1.png" alt="Picture1" border="0"></a>

<h2>Features</h2>

<ul>
  <li>Custom user model for managing user registration and authentication</li>
  <li>JWT token-based authentication for secure user sessions</li>
  <li>Integration with Stripe for processing payments</li>
  <li>Business listing management with create, read, update, and delete operations</li>
  <li>Filtering and sorting options for business listings</li>
  <li><strong>Once a business is purchased through Stripe, it is automatically removed from the available business listings</strong></li>
  <li>Permissions and authorization management for protected endpoints</li>
</ul>

<h2>Pictures</h2>

<div> 
<a href="https://ibb.co/hXFdHTg"><img src="https://i.ibb.co/hXFdHTg/Picture4.png" alt="Picture4" border="0"></a>

<a href="https://ibb.co/3knQ6qX"><img src="https://i.ibb.co/3knQ6qX/Picture3.png" alt="Picture3" border="0"></a>
  </div>
<div>
  <a href="https://ibb.co/6yMj83c"><img src="https://i.ibb.co/7SfsQwx/Picture5.png" alt="Picture5" border="0"></a><br /><a target='_blank' href='https://imgbb.com/'></a><br />
</div>

<h2>Project Structure</h2>

<p>The backend project follows a typical structure for a Django application:</p>

<ul>
  <li><code>bizdeals/</code>: Root directory for the project
    <ul>
      <li><code>userapp/</code>: Django app for user-related functionality</li>
      <li><code>businessapp/</code>: Django app for business listing functionality</li>
      <li><code>requirements.txt</code>: List of project dependencies</li>
    </ul>
  </li>
</ul>

<h2>Getting Started</h2>

<p>To run the BizDeals backend on your local machine, follow these steps:</p>

<ol>
  <li>Clone the repository:</li>

  <pre><code>git clone https://github.com/Hassan01SE/BizDeals-BACK-END-.git</code></pre>
   <li>Create and activate a virtual environment (optional but recommended):</li>

  <pre><code>python -m venv env
source env/bin/activate</code></pre>

  <li>Install the required dependencies:</li>

  <pre><code>cd bizdeals-backend
pip install -r requirements.txt</code></pre>

  <li>Set up the database and run migrations:</li>

  <pre><code>python manage.py migrate</code></pre>

  <li>Start the development server:</li>

  <pre><code>python manage.py runserver</code></pre>

  <li>The backend server will be running at <code>http://localhost:8000</code>.</li>
</ol>

<h2>Dependencies</h2>

<p>The backend project utilizes the following libraries and dependencies:</p>

<ul>
  <li>Django: High-level Python web framework</li>
  <li>Django REST Framework: Toolkit for building RESTful APIs with Django</li>
  <li>Django Rest Framework Simple JWT: Library for JSON Web Token authentication</li>
  <li>Stripe: Payment processing library</li>
  <li>Other dependencies listed in <code>requirements.txt</code></li>
</ul>

<p><em>This project is licensed under the MIT License.</em></p>
