import { shallow } from 'enzyme';
import React from 'react';
import Sidebar3 from '../pages/Teacher';
import axiosInstance from '../utlities/axiosInstance';

jest.mock('../utlities/axiosInstance');

describe('Sidebar3', () => {
  let wrapper;

  const students = [    { id: 1, username: 'John Doe' },    { id: 2, username: 'Jane Smith' },  ];

  const parent = { id: 1, username: 'Teacher' };

  const undone = [    { id: 1, name: 'Lesson 1' },    { id: 2, name: 'Lesson 2' },  ];

  const done = [    { id: 3, name: 'Lesson 3' },    { id: 4, name: 'Lesson 4' },  ];

  beforeEach(() => {
    axiosInstance.get.mockImplementation((url) => {
      switch (url) {
        case 'teachers/1/':
          return Promise.resolve({ data: parent });
        case 'students/':
          return Promise.resolve({ data: students });
        case 'unfinished/1/lessons/':
          return Promise.resolve({ data: undone });
        case 'finished/1/lessons/':
          return Promise.resolve({ data: done });
        default:
          return Promise.reject(new Error('not found'));
      }
    });
    wrapper = shallow(<Sidebar3 />);
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it('renders the component', () => {
    expect(wrapper.exists()).toBe(true);
  });
});
