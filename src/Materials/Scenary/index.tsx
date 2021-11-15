import React, { useEffect, useRef, useState } from 'react';
import { sprites } from '../Assets';
import { Container } from './styles';
import {JavaScript} from './javaScript';

// interface ITerrain {
//   sprite: HTMLImageElement;
//   width: number;
//   height: number;
//   positionX: number;
//   positionY: number;
//   // render: (x: number, y: number) => void;
// }

// interface IDrawImage {
//   sprite: HTMLImageElement;
//   width: number;
//   height: number;
//   positionX: number;
//   positionY: number;
// }

// interface IstepsTerrain {
//   positionX: number;
//   positionY: number;
// }

export const Scenary = () => {
  // const canvasRef = useRef<HTMLCanvasElement | null>(null);
  // const canvasCtxRef = useRef<CanvasRenderingContext2D | null>(null);
  // const requestRef = React.useRef<number>(0);
  // const [previousTime, setPreviousTime] = useState(0);
  // const [count, setCount] = useState(0);


 
  // // useEffect(() => {

  //   if (canvasRef.current) {
  //     canvasCtxRef.current = canvasRef.current.getContext('2d');
  //   }
  
  //   const ctx = canvasCtxRef.current;
  //   const spriteTerrain = new Image();
  //   spriteTerrain.src = sprites.ground_rocky;

  //   if (ctx) {
  //     console.log('Boara caralho!!');
  //     console.log('width: ', spriteTerrain.width)
  //     console.log('height: ', spriteTerrain.height)
  //     console.log('spriteTerrain: ', spriteTerrain)


  //     ctx!.drawImage(
  //       spriteTerrain,
  //       50,
  //       50,
  //       50,
  //       50,
  //     );
  //   }
  //   console.log('CTX Não existe');

  // // }, []);

  // useEffect(() => {
  //   console.log(previousTime)

  // },[previousTime])

  // const animate = (time: number) => {

  //   if (canvasRef.current) {
  //     canvasCtxRef.current = canvasRef.current.getContext('2d');
  //   }

  //   const spriteTerrain = new Image();
  //   spriteTerrain.src = sprites.ground_rocky;

  //   const ctx = canvasCtxRef.current;
  //   if(previousTime != 0){
  //     const deltaTime = time - previousTime;
  //     setCount(prevCount => (prevCount + deltaTime * 0.00001) % 100);
  //     if (ctx) {
  //       ctx.clearRect(0, 0, 300, 300);

  //       ctx!.drawImage(
  //           spriteTerrain,
  //           count,
  //           10,
           
  //         );
  //     }
  //   }
  //   setPreviousTime(time)
  //   requestRef.current = requestAnimationFrame(animate);
  // }

  // useEffect(() => {
  //   requestRef.current = requestAnimationFrame(animate);
  //   return () => cancelAnimationFrame(requestRef.current);
  
  // }, []); 

  return (
    <Container>
      {/* <button onClick={() => setRender(render!)}>Renderizar</button> */}
      {/* <canvas ref={canvasRef}></canvas> */}
      <JavaScript/>
    </Container>
  );
};
