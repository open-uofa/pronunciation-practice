import React from 'react';
import { shallow } from 'enzyme';
import Chapter from '../components/Teacher/Chapter';
import Lesson from '../components/Teacher/Lesson';
import '../setupTests';


describe('Chapter component', () => {
  const props = {
    lessons: [
      { id: 1, title: 'Lesson 1', content: 'This is lesson 1' },
      { id: 2, title: 'Lesson 2', content: 'This is lesson 2' },
      { id: 3, title: 'Lesson 3', content: 'This is lesson 3' },
    ],
    student: '123',
  };

  it('renders a list of lessons', () => {
    const wrapper = shallow(<Chapter {...props} />);
    expect(wrapper.find(Lesson).length).toEqual(props.lessons.length);
  });

  it('passes correct props to each Lesson component', () => {
    const wrapper = shallow(<Chapter {...props} />);
    wrapper.find(Lesson).forEach((node, index) => {
      expect(node.props().lesson).toEqual(props.lessons[index]);
      expect(node.props().student).toEqual(props.student);
    });
  });
});