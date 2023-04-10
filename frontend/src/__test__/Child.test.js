import React from 'react';
import { shallow } from 'enzyme';
import Child from '../pages/Child';

describe('Child component', () => {
  const childName = 'Test Child';
  const lessons = [{ id: 1, title: 'Test Lesson 1' }, { id: 2, title: 'Test Lesson 2' }];

  it('should render correctly', () => {
    const wrapper = shallow(<Child childName={childName} lessons={lessons} />);
    expect(wrapper.exists()).toBeTruthy();
  });

  it('should render the child name', () => {
    const wrapper = shallow(<Child childName={childName} lessons={lessons} />);
    expect(wrapper.find('h1').text()).toEqual(`${childName}'s Lessons:`);
  });
});