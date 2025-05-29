import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { signup } from '../services/auth';

export default function Signup() {
  const [username, setUsername] = useState('');
  const [email, setEmail]       = useState('');
  const [password, setPassword] = useState('');
  const [error, setError]       = useState(null);
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      await signup(username, email, password);
      navigate('/login');
    } catch {
      setError('Signup failed');
    }
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="max-w-md mx-auto bg-white p-6 rounded shadow"
    >
      <h1 className="text-2xl mb-4">Sign Up</h1>
      {error && <p className="text-red-500 mb-2">{error}</p>}

      <input
        placeholder="Username"
        value={username}
        onChange={e => setUsername(e.target.value)}
        className="w-full p-2 mb-3 border rounded"
      />

      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        className="w-full p-2 mb-3 border rounded"
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={e => setPassword(e.target.value)}
        className="w-full p-2 mb-3 border rounded"
      />

      <button
        type="submit"
        className="w-full p-2 bg-green-600 text-white rounded"
      >
        Sign Up
      </button>

      <p className="mt-4 text-center">
        Already have an account?{' '}
        <Link to="/login" className="text-blue-600">
          Log in
        </Link>
      </p>
    </form>
  );
}
