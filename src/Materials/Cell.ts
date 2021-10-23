import { TerrainType } from './TerrainType';

export interface ICell {
  index: number;
  positionY: number;
  positionX: number;
  left: Cell | null;
  right: Cell | null;
  up: Cell | null;
  down: Cell | null;
  coins?: number;
  terrainType: TerrainType;
}

export class Cell {
  index: number;
  positionY: number;
  positionX: number;
  left: Cell | null;
  right: Cell | null;
  up: Cell | null;
  down: Cell | null;
  coins?: number;
  terrainType: TerrainType;

  constructor(props: ICell) {
    const { index, positionX, positionY, left, right, up, down, coins, terrainType } = props;
    this.index = index;
    this.positionX = positionX;
    this.positionY = positionY;
    this.left = left;
    this.right = right;
    this.up = up;
    this.down = down;
    this.coins = coins;
    this.terrainType = terrainType;

  }

}
