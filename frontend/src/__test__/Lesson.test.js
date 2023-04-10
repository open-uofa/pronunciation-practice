import Lesson from '../components/Teacher/Lesson';
import StudentLesson from '../components/StudentParent/Lesson';
import { shallow } from 'enzyme';
import '../setupTests';


describe('Teacher lesson component', () => {
  const studentId = '123';
  const lesson = {
    id: 1,
    text: 'example lesson text',
    has_image: false,
    status: 'completed',
  };

  it('should render a div containing the generated lesson', () => {
    const wrapper = shallow(<Lesson student={studentId} lesson={lesson} />);
    expect(wrapper.find('div').length).toBe(1);
  });
});

describe('Student lesson component', () => {
  const lessonCompleted = {
    id: 1,
    text: 'example lesson text',
    has_image: false,
    status: 'completed',
  };

  const student = {
    id: 1,
    username: 'jdoe',
    first_name: 'John',
    last_name: 'Doe',
  }

  it('should render a div containing the generated lesson marked as completed', () => {
    const wrapper = shallow(<StudentLesson lesson={lessonCompleted} student={student} status={"Completed"} />);
    expect(wrapper.exists()).toBe(true);
  });
});