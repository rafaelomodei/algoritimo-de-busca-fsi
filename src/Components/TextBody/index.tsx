import { Container } from "./styles"

interface ITextBody{
    text: string;
}

export const TextBody = ({text}: ITextBody) => {
    return (
        <Container>
           {text}
        </Container>
    );
}