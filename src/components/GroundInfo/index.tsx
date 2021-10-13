import { Container } from './styles';

interface GroundInfoProps {
  children: React.ReactNode;
}

export const GroundInfo = ({ children }: GroundInfoProps) => {
  return <Container>{children}</Container>;
};
