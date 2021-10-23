import styled from 'styled-components';
import { Paper } from '../Paper';

export const Container = styled(Paper)`
Footer`;

export const Content = styled.div``;

export const Children = styled.div`
  display: flex;

  div:not(:first-child) {
    margin-left: 20px;
  }
`;
