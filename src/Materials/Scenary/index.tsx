import SimplexNoise from 'simplex-noise';
import React, { useEffect, useRef, useState } from 'react';
import { sprites } from '../Assets';

import { Container } from './styles';

interface ITerrain {
  sprite: HTMLImageElement;
  width: number;
  height: number;
  positionX: number;
  positionY: number;
  render: (x: number, y: number) => void;
}

interface IstepsTerrain {
  positionX: number;
  positionY: number;
}

export const Scenary = () => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const canvasCtxRef = useRef<CanvasRenderingContext2D | null>(null);
  const requestRef = useRef<number>(0);

  const spriteTerrain = new Image();

  const stepsTerrain: IstepsTerrain = {
    positionX: 73 / 2,
    positionY: 43 / 2,
  };

  const createTerrain = () => {
    let ctx = canvasCtxRef.current;

    const randonTerrain = (value: number) => {
      value <= 0.2
        ? (spriteTerrain.src = sprites.ground_wood)
        : value > 0.2 && value <= 0.4
        ? (spriteTerrain.src = sprites.ground_sandy)
        : value > 0.4 && value <= 0.6
        ? (spriteTerrain.src = sprites.ground_rocky)
        : (spriteTerrain.src = sprites.ground_swamp);
      return spriteTerrain;
    };

    const simplex = new SimplexNoise();
    const value = simplex.noise2D(Math.random() / 6, Math.random() / 6);
    let spriteR = randonTerrain(value);

    const terrain: ITerrain = {
      sprite: spriteR,
      width: spriteTerrain.width,
      height: spriteTerrain.height,
      positionX: 0,
      positionY: 0,
      render: (x, y) => {
        ctx!.drawImage(
          terrain.sprite,
          terrain.positionX + terrain.positionX * x,
          terrain.positionY + terrain.positionY * y,
          terrain.width,
          terrain.height
        );
      },
    };
  };

  const useAnimationFrame = (callback: Function) => {
    // Use useRef for mutable variables that we want to persist
    // without triggering a re-render on their change
    const requestRef = useRef<number>(0);
    const previousTimeRef = useRef<number>();
    /**
     * The callback function is automatically passed a timestamp indicating
     * the precise time requestAnimationFrame() was called.
     */

      useEffect(() => {
      const animate = (time: number) => {
        if (previousTimeRef.current !== undefined) {
          const deltaTime = time - previousTimeRef.current;
          callback(deltaTime);
        }
        previousTimeRef.current = time;
        requestRef.current = requestAnimationFrame(animate);
      };
      requestRef.current = requestAnimationFrame(animate);
      return () => cancelAnimationFrame(requestRef.current);
    }, []); // Make sure the effect runs only once
  };

  const [count, setCount] = useState(0);

  useAnimationFrame((deltaTime: number) => {

    if (canvasRef.current) {
      canvasCtxRef.current = canvasRef.current.getContext('2d');
      createTerrain();
    }

    setCount(prevCount => (prevCount + deltaTime * 0.001) % 100);
  });

  return (
    <Container>
      {count}
      <canvas ref={canvasRef}></canvas>
    </Container>
  );
};
