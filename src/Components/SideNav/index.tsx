import { BiChevronLeft, BiChevronRight } from 'react-icons/bi';
import { Title } from '../Title';

import { Container, Content } from './styles';

interface SideNavProps {
  isOpen: boolean;
  children: React.ReactNode;
  onRequestClose: () => void;
}

export const SideNav = ({ isOpen, onRequestClose, children }: SideNavProps) => {
  const isOpenSideNav = isOpen ? 'openSideNav' : '';
  return (
    <Container className={isOpenSideNav}>
        <Content className={isOpenSideNav}>
          {Boolean(isOpenSideNav.length) && children}
        
        <button
          type='button'
          className={isOpenSideNav}
          onClick={onRequestClose}
        >
          {isOpenSideNav.length ? (
            <BiChevronLeft color='white' fontSize='46' />
          ) : (
            <BiChevronRight color='white' fontSize='46' />
          )}
        </button>
        </Content>
    </Container>
  );
};
