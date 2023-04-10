import axiosInstance from '../utlities/axiosInstance';

describe('axiosInstance', () => {
  it('should have the correct baseURL', () => {
    expect(axiosInstance.defaults.baseURL).toEqual('http://localhost:8000');
  });

  it('should have a timeout of 5000ms', () => {
    expect(axiosInstance.defaults.timeout).toEqual(5000);
  });
});
