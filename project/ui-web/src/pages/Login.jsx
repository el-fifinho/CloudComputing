import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { login } from '../services/auth';

export default function Login() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [pass, setPass] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      await login(username, email, pass);
      navigate('/');
    } catch {
      setError('Invalid credentials');
    }
  }

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto bg-white p-6 rounded shadow">
      <h1 className="text-2xl mb-4">Login</h1>
      {error && <p className="text-red-500 mb-2">{error}</p>}
      <input placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} className="w-full p-2 mb-3 border rounded" />
      <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} className="w-full p-2 mb-3 border rounded" />
      <input type="password" placeholder="Password" value={pass} onChange={e => setPass(e.target.value)} className="w-full p-2 mb-3 border rounded" />
      <button type="submit" className="w-full p-2 bg-blue-600 text-white rounded">Log In</button>
      <p className="mt-4 text-center">
        Don't have an account? <Link to="/signup" className="text-blue-600">Sign up</Link>
      </p>
    </form>
  );
}
