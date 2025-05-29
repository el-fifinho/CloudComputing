import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { request } from '../services/api';

export default function Fields() {
  const [fields, setFields] = useState([]);
  const [sportId, setSportId] = useState('');

  useEffect(() => {
    fetchFields();
  }, []);

  async function fetchFields() {
    const q = sportId ? `?sport_id=${sportId}` : '';
    const data = await request(`/fields${q}`);
    setFields(data);
  }

  return (
    <div>
      <h1 className="text-xl mb-4">Sport Fields</h1>
      <div className="mb-4">
        <input placeholder="Sport ID" value={sportId} onChange={e => setSportId(e.target.value)} className="p-2 border rounded mr-2" />
        <button onClick={fetchFields} className="p-2 bg-gray-500 text-white rounded">Search</button>
      </div>
      <ul className="space-y-2">
        {fields.map(f => (
          <li key={f.field_id} className="bg-white p-4 rounded shadow">
            <Link to={`/fields/${f.field_id}`} className="text-blue-600">{f.name}</Link>
            <p className="text-sm">Price/hr: {f.price_per_hour}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}