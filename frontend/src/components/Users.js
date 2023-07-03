import { useState, useEffect } from "react";
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import { useNavigate, useLocation, json } from "react-router-dom";
import axios from "../api/axios";
import useAuth from "../hooks/useAuth";

const Users = () => {
  const { auth } = useAuth();
  const [users, setUsers] = useState();
  const axiosPrivate = useAxiosPrivate();
  const navigate = useNavigate();
  const location = useLocation();

  // let isMounted = true;
  // const controller = new AbortController();

  useEffect(() => {
    const token = auth.accessToken;
    console.log(token);
    console.log(auth);
    const authToken = {
      "Content-Type": "application/json",
      Headers: { Authorization: `Bearer ${token}` },
    };

    try {
      fetch("http://127.0.0.1:8000/api/users/list", {
        "Content-Type": "application/json",
        Headers: { Authorization: `Bearer ${auth.accessToken}` },
      })
        .then((response) => JSON.stringify(response.data))
        .then((data) => console.log(data));
    } catch (error) {
      console.log(error);
    }
  }, []);

  // const getUsers = async () => {
  // try {
  //   const response = await axios.get("api/users/list", {
  //     headers: {
  //       // "Content-Type": "application/json",
  //       Authorization: `Bearer ${auth.accessToken}`,
  //     },
  //   });
  //   console.log(response.data);
  //   setUsers(response.data);
  // } catch (error) {
  //   console.error(error);
  //   throw error;
  // }
  // try {
  //   const response = await axiosPrivate.get("api/users/list", {
  //     signal: controller.signal,
  //   });
  //   console.log(response.data);
  //   isMounted && setUsers(response.data);
  // } catch (err) {
  //   console.error(err);
  //   navigate("/login", { state: { from: location }, replace: true });
  // }
  // return () => {
  //   isMounted = false;
  //   controller.abort();
  // };
  // };
  // getUsers();

  return !users ? (
    <h1>Could not render the users list</h1>
  ) : (
    users.results.map((item) => <li>{item.username}</li>)
  );

  // <article>
  //   <h2>Users List</h2>
  //   {users?.length ? (
  //     <ul>
  //       {users.map((user, i) => (
  //         <li key={i}>{user?.username}</li>
  //       ))}
  //     </ul>
  //   ) : (
  //     <p>No users to display</p>
  //   )}
  // </article>
};

export default Users;
