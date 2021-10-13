import styled from 'styled-components';

export const Container = styled.div`
  display: flex;
  height: 100%;
  position: fixed;
  z-index: 999;
  overflow-x: hidden;
  transition: 0.2s;

  button {
    align-items: center;
    justify-content: center;
    border: none;
    width: 60px;
    height: 100%;

    background-color: #141414;
  }
  
`;

export const Content = styled.div`
  display: flex;
  height: 100%;
  width: 0px;
  position: fixed;
  left: 0;
  background: white;
  /* transition: width 0.2s; */
  
  &.openSideNav {
    width: 600px;
  }
`;
