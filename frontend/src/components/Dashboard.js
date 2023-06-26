import React from 'react'
import { NavLink } from 'react-router-dom'
import './DashboardStyles.css'
const Dashboard = () => {
  return (
    <div>
      <h1>Dashboard</h1>
      <nav className='dashboard-nav'>
        <ul>
          <NavLink to='/admin/clients'>Clients</NavLink>
          <li>Orders</li>
          <li>Products</li>
          <li>Graphs</li>
          <li>Inventory</li>
        </ul>
      </nav>
    </div>
  )
}

export default Dashboard
