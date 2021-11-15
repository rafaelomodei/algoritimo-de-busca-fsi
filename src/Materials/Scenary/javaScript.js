import { spritesPng } from '../Assets';


// interface ITerrain {
//     sprite: HTMLImageElement;
//     width: number;
//     height: number;
//     positionX: number;
//     positionY: number;
//   }


export const JavaScript = () => {

    const terrain = new Image();
    terrain.src = spritesPng.ground_solid;


    const canvas = document.querySelector('canvas');
    const context = canvas?.getContext('2d');
    
    const terrainSolid = {
        spriteX: 0,
        spriteY: 0,
        width: 70,
        height: 46,
        x: 10,
        y: 10,
        desenha() {
            context?.drawImage(
                terrain,
                terrainSolid.spriteX, terrainSolid.spriteY,
                terrainSolid.width, terrainSolid.height,
                terrainSolid.x, terrainSolid.y,
                terrainSolid.width, terrainSolid.height,
            );
        }
    }


    function loop(){
        console.log('loop')
        terrainSolid.desenha()

        requestAnimationFrame(loop);
    }

    loop();


    return <canvas id="game-canvas">JavaScript</canvas>
}
