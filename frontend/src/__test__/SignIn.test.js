import React from 'react';
import { shallow } from 'enzyme';
import SignIn from '../pages/SignIn';

jest.mock('react-router-dom', () => ({
  useNavigate: jest.fn(),
}));

describe('SignIn', () => {
  it('should render the login page', () => {
    const wrapper = shallow(<SignIn />);
    expect(wrapper.exists()).toBeTruthy();
  });
});

