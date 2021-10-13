import { TextBody } from '../TextBody';
import { Title } from '../Title';
import { Container, Content, Children } from './styles';

interface InformationProps {
  title: string;
  subtitle: string;
  children: React.ReactNode;
}

export const Information = ({
  title,
  subtitle,
  children,
}: InformationProps) => {
  return (
    <Container>
      <Content>
        <div>
          <Title text={title} />
          <TextBody text={subtitle} />
        </div>
        <Children>{children}</Children>
      </Content>
    </Container>
  );
};
