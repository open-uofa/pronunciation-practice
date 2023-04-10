function logout() {
  // localStorage.removeItem('access_token');
  // localStorage.removeItem('refresh_token');
  // localStorage.removeItem('id');
  // localStorage.removeItem('role');
  localStorage.clear();
  window.location.reload();
  window.location.href = '/login';
}
export default logout;