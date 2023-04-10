import React from 'react';
import { createRoot } from 'react-dom/client';
import App from '../App';
import { shallow } from 'enzyme';

describe('App component', () => {
  it('renders without crashing', () => {
    const app = shallow(<App />);
    expect(app).toMatchSnapshot();
  });
});