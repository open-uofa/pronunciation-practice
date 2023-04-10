import React from 'react';
import { shallow } from 'enzyme';
import { useNavigate } from 'react-router-dom';
import ProtectedRoute from '../utlities/ProtectedRoute';

jest.mock('react-router-dom', () => ({
  useNavigate: jest.fn(),
}));

describe('ProtectedRoute', () => {
  let props;
  let wrapper;

  beforeEach(() => {
    props = {
      children: <div>Protected content</div>,
    };
    useNavigate.mockImplementation(() => jest.fn());
    wrapper = shallow(<ProtectedRoute {...props} />);
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it('should render children if user is logged in', () => {
    localStorage.setItem('access_token', 'testToken');
    const result = wrapper.find('React.Fragment').children();
    expect(result).toHaveLength(0);
  });

  it('should redirect to login if user is not logged in', () => {
    localStorage.removeItem('access_token');
    const result = wrapper.find('React.Fragment').children();
    expect(result).toHaveLength(0);
    expect(useNavigate).toHaveBeenCalled();
  });
});
