import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import './menu.css';
import {Route,Routes,BrowserRouter,Link} from 'react-router-dom';
import App from './App';
import Users from './users';
import Contact from './contact';
import Menu from './menu';
import Notfound  from './notfound';

const routing = (
  <div>
    <BrowserRouter>
      <nav id="nav" class="wrap">
        <div class="navbar-header">
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/usuarios">Users</Link>
            </li>
            <li>
              <Link to="/contacto">Contact</Link>
            </li>
            <li>
              <Link to="/menu">Ejemplo del Menu</Link>
            </li>
          </ul>
        </div>
      </nav>
      <Routes>
        <Route exact path="/" element={<App />} />
        <Route path="/usuarios/:id" element={<Users />} />
        <Route path="/contacto" element={<Contact />} />
        <Route path="/menu" element={<Menu />} />
        <Route path="/notfound" element = {<Notfound />} />
      </Routes>
    </BrowserRouter>
  </div>
)

ReactDOM.render(
  routing,
  document.getElementById('root')
);





