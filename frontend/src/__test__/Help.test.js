import React from 'react';
import { shallow } from 'enzyme';
import Help from '../pages/Help';

describe('Help', () => {
  it('should render the component for the student role', () => {
    const wrapper = shallow(<Help role={"Student"}/>);
    expect(wrapper.exists()).toBe(true);
  });

  it('should render the component for the parent role', () => {
    const wrapper = shallow(<Help role={"Parent"}/>);
    expect(wrapper.exists()).toBe(true);
  });
});