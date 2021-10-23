import { Cell, ICell } from './Cell';
import { ScenaryGeneratorSatate } from './ScenaryGeneratorSatate';
import { TerrainType } from './TerrainType';

export class ScenaryControllerState {
  start() {

    // const propsCell:ICell = {
    //     index: 0,

    //     left: 1,
    //     right: 2,
    //     up: 3,
    //     down: 4,
    //     coins: 5,
    //     terrainType: TerrainType.Rochoso
    // }
    const cenary = new ScenaryGeneratorSatate();
    // const cell = new Cell(propsCell);
    console.log('Inicalizando game...');
    // console.log('cell: ', cell);
    console.log('cenary: ', cenary.start());
  }
}
