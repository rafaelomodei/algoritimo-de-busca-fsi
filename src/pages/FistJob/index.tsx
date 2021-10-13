import { Card } from '../../components/Card';
import { svg } from '../../assets';
import { Container, InfoButtom, InfoTop, Footer } from './styles';
import { SideNav } from '../../components/SideNav';
import { useState } from 'react';
import { Information } from '../../components/information';
import { GroundInfo } from '../../components/GroundInfo';
import { TextBody } from '../../components/TextBody';
import { Image } from '../../components/Image';
import { Title } from '../../components/Title';

export const FistJob = () => {
  const [isSideNav, setIsSideNav] = useState(false);
  const toggleIsSideNav = () => {
    console.log(`handleOpenIsSideNav:: ${isSideNav}`);
    setIsSideNav(!isSideNav);
  };

  return (
    <Container>
      <SideNav isOpen={isSideNav} onRequestClose={toggleIsSideNav}>
        <Information title='Informações' subtitle='Tipos de terronos'>
          <GroundInfo>
            <TextBody text='Sólido e plano' />
            <Image img={svg.ground_wood} />
            <TextBody text={`Custo: +${1} `} />
          </GroundInfo>

          <GroundInfo>
            <TextBody text='Arenosos' />
            <Image img={svg.ground_sandy} />
            <TextBody text={`Custo: +${4} `} />
          </GroundInfo>

          <GroundInfo>
            <TextBody text='Rochoso' />
            <Image img={svg.ground_rocky} />
            <TextBody text={`Custo: +${10} `} />
          </GroundInfo>

          <GroundInfo>
            <TextBody text='Pântano' />
            <Image img={svg.ground_swamp} />
            <TextBody text={`Custo: +${20} `} />
          </GroundInfo>
        </Information>
      </SideNav>
      <InfoTop>
        <Card img={svg.clock} title={`Tempo de execução`} text={`01:30:20`} />
      </InfoTop>
      <Footer>
          <InfoButtom>
            <Card
              img={svg.node}
              title={`Total de nós expandidos`}
              text={`350`}
            />
            <Card
              img={svg.heuristic}
              title={`Heurística`}
              text={`Algoritmos Guloso`}
            />
            <Card img={svg.reward} title={`Total de recompensa`} text={`20`} />
          </InfoButtom>
      </Footer>
    </Container>
  );
};
