import { Card } from '../../Components/Card';
import { svg } from '../../Assets';
import { Container, InfoButtom, InfoTop, ScenaryContainer, Footer } from './styles';
import { SideNav } from '../../Components/SideNav';
import { useEffect, useState } from 'react';
import { Information } from '../../Components/Information';
import { GroundInfo } from '../../Components/GroundInfo';
import { TextBody } from '../../Components/TextBody';
import { Image } from '../../Components/Image';
import { Title } from '../../Components/Title';
import { Scenary } from '../../Materials/Scenary';
import api from '../../services/api';


export const FistJob = () => {
  const [isSideNav, setIsSideNav] = useState(false);
  const toggleIsSideNav = () => {
    console.log(`handleOpenIsSideNav:: ${isSideNav}`);
    setIsSideNav(!isSideNav);
  };

  useEffect(() => {
    try {
    
      api.get('/countries').then(response => console.log(response));
      
    } catch (error) {
      console.log('DEu ruim: ', error);
    }
  }, []);

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
      <header>
        <InfoTop>
          <Card img={svg.clock} title={`Tempo de execução`} text={`01:30:20`} />
        </InfoTop>
      </header>

      <ScenaryContainer>
        <Scenary />
        {/* <button onClick={handlerScenary}>Carregar cenario</button> */}
      </ScenaryContainer>
      <Footer>
        <InfoButtom>
          <Card img={svg.node} title={`Total de nós expandidos`} text={`350`} />
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
