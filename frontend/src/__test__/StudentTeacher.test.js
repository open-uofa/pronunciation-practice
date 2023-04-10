import React from 'react';
import { shallow } from 'enzyme';
import Student from '../components/Teacher/Student';


describe('Student', () => {
    it('should render without crashing', () => {
        const wrapper = shallow(<Student />);
        expect(wrapper.exists()).toBe(true);
    });
});