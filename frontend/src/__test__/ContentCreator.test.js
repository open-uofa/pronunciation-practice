import { shallow } from 'enzyme';
import Sidebar4 from '../pages/Content_Creator';
import '../setupTests';


describe('Sidebar4', () => {
  it('should render with initial state', () => {
    const wrapper = shallow(<Sidebar4 />);
    expect(wrapper.exists()).toBeTruthy();
  });
});