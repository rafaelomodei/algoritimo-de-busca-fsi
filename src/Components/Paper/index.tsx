import { Container } from './styles';

interface PaperProps {
  children: React.ReactNode;
}

export const Paper = ({ children }: PaperProps) => {
  return <Container>{children}</Container>;
};
