import { Container } from './styles';

interface AvatarProps {
  img: string;
}

export const Avatar = ({ img }: AvatarProps) => {
  return (
    <Container>
      <img src={img} />
    </Container>
  );
};
