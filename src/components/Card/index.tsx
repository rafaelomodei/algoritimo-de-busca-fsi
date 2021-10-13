import { Avatar } from '../Avatar';
import { Paper } from '../Paper';
import { TextBody } from '../TextBody';
import { Container } from './styles';

interface CardProps {
  img: string;
  title: string;
  text: string;
}

export const Card = ({ img, title, text }: CardProps) => {
  return (
    <Paper>
      <Container>
        <Avatar img={img} />
        <div>
          <TextBody text={title} />
          <b>
            <TextBody text={text} />
          </b>
        </div>
      </Container>
    </Paper>
  );
};
