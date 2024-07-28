// src/components/SailorList.js
import React, { useEffect, useState } from 'react';
import { fetchSailors } from '../services/api';

const SailorList = () => {
  const [sailors, setSailors] = useState([]);

  useEffect(() => {
    const getSailors = async () => {
      const response = await fetchSailors();
      setSailors(response.data);
    };

    getSailors();
  }, []);

  return (
    <div>
      <h1>Sailors</h1>
      <ul>
        {sailors.map((sailor) => (
          <li key={sailor.id}>{sailor.firstname} {sailor.lastname}</li>
        ))}
      </ul>
    </div>
  );
};

export default SailorList;

