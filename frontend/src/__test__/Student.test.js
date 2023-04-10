import React from 'react';
import { shallow } from 'enzyme';
import SideBarStudentLesson from '../pages/Student';

describe('SideBarStudentLesson', () => {
  it('should render the component without errors', () => {
    const wrapper = shallow(<SideBarStudentLesson chapter={{ lessons: [] }} />);
    expect(wrapper.exists()).toBe(true);
  });
});
