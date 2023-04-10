import React from 'react';
import { shallow } from 'enzyme';
import HomeLessonTab from '../components/StudentParent/HomeLessonTab';


const testTab = {
    "id": "9928fbf8-1b6b-43e4-b1a0-2cf5674a2551",
    "name": "Lesson Tab 1",
    "chapters": [
        {
            "id": "fa3b733c-8177-4145-8ade-8113849aee3c",
            "name": "Chapter 1",
            "tab": "9928fbf8-1b6b-43e4-b1a0-2cf5674a2551",
            "lessons": [
                {
                    "id": "0893f873-b918-4c75-8c6c-443ccddf2832",
                    "text": "/media/Hello%20World",
                    "audio": "/media/audio1.mp3",
                    "has_image": false,
                    "chapter": "fa3b733c-8177-4145-8ade-8113849aee3c",
                    "status": "assigned"
                },
                {
                    "id": "1e367b42-a097-4ef6-b610-c33dc4008f26",
                    "text": "/media/This%20is%20the%20first%20chapter.",
                    "audio": "/media/lesson2.mp3",
                    "has_image": false,
                    "chapter": "fa3b733c-8177-4145-8ade-8113849aee3c",
                    "status": "unassigned"
                },
                {
                    "id": "3a4c8488-7b6e-4f4e-a2eb-533e2f4dd3ec",
                    "text": "/media/This%20lesson%20is%20the%20last%20one%20in%20the%20chapter.",
                    "audio": "/media/lesson3.mp3",
                    "has_image": false,
                    "chapter": "fa3b733c-8177-4145-8ade-8113849aee3c",
                    "status": "completed"
                }
            ]
        }
    ]
};

describe('HomeLessonTab', () => {
    it('should render correctly', () => {
        const wrapper = shallow(<HomeLessonTab tab={testTab} role={"Student"} />);
        expect(wrapper).toMatchSnapshot();
    });
});