import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        console.log('Users API endpoint:', apiUrl);
        console.log('Fetched users:', data);
        setUsers(data.results || data);
      });
  }, [apiUrl]);

  return (
    <div>
      <h2 className="text-primary mb-3">Users</h2>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>Username</th>
            <th>Email</th>
            <th>Team</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user, idx) => (
            <tr key={idx}>
              <td>{user.username}</td>
              <td>{user.email}</td>
              <td>{user.team}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button className="btn btn-primary" onClick={() => window.location.reload()}>Refresh</button>
    </div>
  );
};

export default Users;
