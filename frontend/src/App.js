import './App.css';

import { Routes, Route } from 'react-router-dom';
import ErrorPage from './components/ErrorPage'
import Home from './components/Home';
import SharedLayout from './components/SharedLayout'
import UserPage from './components/UserPage';
import Orders from './components/Orders';
import Cart from './components/Cart';
import SingleProduct from './components/SingleProduct'
import Register from './components/Register';
import DashboardSharedLayout from './components/DashboardSharedLayout';
import Dashboard from './components/Dashboard';
import DashboardClients from './components/DashboardClients'

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<SharedLayout/>}>
          <Route index element={<Home/>}></Route>
          <Route path='orders' element={<Orders/>}></Route>
          <Route path='products/:productId' element={<SingleProduct/>}></Route>
          <Route path='user' element={<UserPage/>}></Route>
          <Route path='cart' element={<Cart/>}></Route>
          <Route path='*' element={<ErrorPage/>}></Route>
          <Route path='register' element={<Register/>}></Route>
          
        </Route>
        <Route path='/admin' element={<DashboardSharedLayout/>}>
          <Route index element={<Dashboard/>}></Route>
          <Route path='clients' element={<DashboardClients/>}></Route>
          <Route path='*' element={<ErrorPage/>}></Route>
        </Route>
      </Routes>

      
    </div>

  );
}

export default App;
