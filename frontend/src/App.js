import "./App.css";

import { Routes, Route } from "react-router-dom";
import ErrorPage from "./components/ErrorPage";
import Home from "./components/Home";
import SharedLayout from "./components/SharedLayout";
import UserPage from "./components/UserPage";
import Orders from "./components/Orders";
import Cart from "./components/Cart";
import SingleProduct from "./components/SingleProduct";
import Register from "./components/Register";
import DashboardSharedLayout from "./components/DashboardSharedLayout";
import Users from "./components/Users";
import Login from "./components/Login";
import RequiredAuth from "./components/RequiredAuth";
import Unauthorized from "./components/Unauthorized";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<SharedLayout />}>
          <Route index element={<Home />}></Route>
          <Route path="orders" element={<Orders />}></Route>
          <Route path="products/:productId" element={<SingleProduct />}></Route>
          <Route path="user" element={<UserPage />}></Route>
          <Route path="cart" element={<Cart />}></Route>
          <Route path="register" element={<Register />}></Route>
          <Route path="login" element={<Login />}></Route>
          <Route path="unauthorized" element={<Unauthorized />} />
          <Route path="users" element={<Users />}></Route>
        </Route>
        <Route element={<RequiredAuth />}>
          <Route path="admin" element={<DashboardSharedLayout />}>
            <Route path="orders"></Route>
            <Route path="products"></Route>
            <Route path="graphs"></Route>
            <Route path="inventory"></Route>
          </Route>
        </Route>
        <Route path="*" element={<ErrorPage />}></Route>
      </Routes>
    </div>
  );
}

export default App;
