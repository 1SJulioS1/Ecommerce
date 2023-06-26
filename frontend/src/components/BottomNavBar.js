import './BottomNavBarStyles.css'
import React from 'react'
import { NavLink } from 'react-router-dom'

const BottomNavBar = () => {
  return (
    <div>
      <navbar className='bottom-nav-bar'>
        <NavLink to='/'>Home</NavLink>
        <NavLink to='user'>User</NavLink>
        <NavLink to='cart'>Cart</NavLink>
        <NavLink to='orders'>Orders</NavLink>
      </navbar>
    </div>
  )
}

export default BottomNavBar
