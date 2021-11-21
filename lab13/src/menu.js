import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
//import './menu.css';
class Menu extends React.Component {
    render() {
      return (
        <div>
            <nav id="nav" class="wrap">
                <input type="checkbox" name="toggle" id="toggle" />
                <label for="toggle"><i class="icon-reorder"></i>Menu</label>
                <ul id="menu">
                    <li>Home</li>
                    <li>Portfolio</li>
                    <li>Services</li>
                    <li>Blog</li>
                    <li>About</li>
                    <li>Contact</li>
                </ul>
            </nav>
        </div>
      )
    }
  }
export default Menu;