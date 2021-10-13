import { Container } from "./styles"

interface ITitle{
    text: string;
}

export const Title = ({text}: ITitle) => {
    return (
        <Container>
           {text}
        </Container>
    );
}