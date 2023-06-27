import './BottomNavBarStyles.css'
import React from 'react'
import { NavLink } from 'react-router-dom'


const BottomNavBar = () => {
  return (
    <div>
      <nav className='bottom-nav-bar'>
        <ul>
          <li>
        <NavLink to='/'>
          <span className="material-symbols-rounded">home</span>
          Home
        </NavLink>
        </li>
        <li>
        <NavLink to='user'><span className="material-symbols-rounded">person</span>
          User
        </NavLink>
        </li>
        <li>
        <NavLink to='cart'><span className="material-symbols-rounded">shopping_cart</span>
          Cart
        </NavLink>
        </li>
        <li>
        <NavLink to='orders'><span className="material-symbols-rounded">fact_check</span>
          Orders
        </NavLink>
        </li>
</ul>
      </nav>
    </div>
  )
}

export default BottomNavBar
