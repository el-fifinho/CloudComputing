import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { request } from '../services/api';

export default function FieldDetail() {
  const { id } = useParams();
  const [field, setField] = useState(null);

  useEffect(() => {
    request(`/fields/${id}`).then(setField);
  }, [id]);

  if (!field) return <p>Loading...</p>;
  return (
    <div className="bg-white p-6 rounded shadow max-w-lg mx-auto">
      <h1 className="text-2xl mb-2">{field.name}</h1>
      <p className="mb-4">{field.description}</p>
      <p className="mb-2">Price per hour: {field.price_per_hour}</p>
      {/* Booking form can go here */}
    </div>
  );
}
