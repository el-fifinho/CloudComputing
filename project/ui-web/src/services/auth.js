import { request } from './api';
export async function login(username, email, password) {
  const data = await request('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ username, email, password })
  });
  localStorage.setItem('token', data.access_token);
}
export async function signup(username, email, password) {
  await request('/auth/signup', {
    method: 'POST',
    body: JSON.stringify({ username, email, password })
  });
}
export function getToken() {
  return localStorage.getItem('token');
}
export function logout() {
  localStorage.removeItem('token');
}