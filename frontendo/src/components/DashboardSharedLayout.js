import { Outlet } from 'react-router-dom'
import React from 'react'
import Dashboard from './Dashboard'

const DashboardSharedLayout = () => {
  return (
    <div>
        <Dashboard></Dashboard>
        <Outlet></Outlet>
    </div>
  )
}

export default DashboardSharedLayout
