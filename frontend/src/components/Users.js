import { useState, useEffect } from "react";
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import { useNavigate, useLocation, json } from "react-router-dom";

import useAuth from "../hooks/useAuth";

const Users = () => {
  const { auth } = useAuth();
  const [users, setUsers] = useState();
  const axiosPrivate = useAxiosPrivate();
  const navigate = useNavigate();
  const location = useLocation();
  const [errMsg, setErrMsg] = useState();

  useEffect(() => {
    let isMounted = true;
    const controller = new AbortController();

    const getUsers = async () => {
      try {
        const response = await axiosPrivate.get("api/users/list", {
          signal: controller.signal,
        });
        console.log(response.data);
        isMounted && setUsers(response.data.results);
        console.log("response received");
      } catch (err) {
        console.error(err);
        // navigate("/login", { state: { from: location }, replace: true });
        // setErrMsg(JSON.stringify(err));
      }
    };

    getUsers();

    return () => {
      isMounted = false;
      controller.abort();
    };
  }, []);

  return (
    <article>
      <h2>Users List</h2>
      <ul>
        {users ? (
          users.map((each, i) => (
            <li key={i} className="text-white bg-black">
              {each.username}
            </li>
          ))
        ) : (
          <li>Loading...</li>
        )}

        {/* <button>
          {users && users.length > 0 ? users[0].username : "No users"}
        </button> */}
      </ul>
    </article>
  );
};

export default Users;
