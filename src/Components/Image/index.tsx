import { Container } from './styles';

interface ImageProps {
  img: string;
}

export const Image = ({ img }: ImageProps) => {
  return (
    <Container>
      <img src={img} />
    </Container>
  );
};
