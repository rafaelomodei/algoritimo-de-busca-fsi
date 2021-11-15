import { Cell, ICell } from './Cell';
import { TerrainType } from './TerrainType';
import { PROBABILITYCREATECOINS, VALUEMAXCOINS } from './constants';

type rangeProbability = 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9;

export class ScenaryGeneratorSatate {
  cell!: Cell;
  referenceMatrix!: Cell;

  headerReferenceColumn!: Cell;
  headerReferenceLine!: Cell;
  
  currentReferenceColumn!: Cell;

  currentReferenceLine!: Cell;


  start(): void { 
    this.spawnScenary(1, 2);
  }

  spawnScenary(lines: number, columns: number): void {
    console.log('line: ', lines, 'width: ', columns);

    let index = 0;

    for (let line = 0; line < lines; line++) {
      for (let column = 0; column < columns; column++) {

        
        const coins = this.createCoins(PROBABILITYCREATECOINS, VALUEMAXCOINS);
        const currentReference = this.createCell(index, line, column, coins);

        console.log(` --- [${ line } , ${ column }] ---  index: ${index}`);
        console.log('NEW currentReference: ', currentReference);
        
        // if(this.referenceMatrix === undefined) {
        //     this.referenceMatrix = currentReference;

        //     console.log('-------------------');
        //     console.log('CREATE::referenceMatrix: ', this.referenceMatrix);
        //     console.log('-------------------');
        // }


        this.currentReferenceColumn = currentReference;
        this.currentReferenceColumn.right = this.currentReferenceColumn;

        this.headerReferenceLine = this.currentReferenceColumn;

        this.headerReferenceLine.right = this.createCell(100, line, column, coins);
        this.headerReferenceLine.left = this.createCell(200, line, column, coins);




        // currentReference. left = this.currentReferenceColumn;

        console.log('-------------------');
        console.log('currentReference: ', currentReference);
        console.log('currentReferenceColumn: ', this.currentReferenceColumn);
        console.log('currentReferenceColumn::right: ', this.currentReferenceColumn.right);
        console.log('headerReferenceLine::left: ', this.headerReferenceLine.left);
        console.log('headerReferenceLine::right: ', this.headerReferenceLine.right);
        console.log('headerReferenceLine:: ', this.headerReferenceLine);

        // console.log('currentReferenceColumn::left: ', this.currentReferenceColumn.left);
        // console.log('currentReferenceColumn::right: ', this.currentReferenceColumn.right);
        console.log('-------------------');
        index++;


      }
    }
  }

  createCell(index: number, positionX: number, positionY: number, coins: number): Cell {
    const propsCell: ICell = {
      index: index,
      positionY: positionX,
      positionX: positionY,
      left: null,
      right: null,
      up: null,
      down: null,
      coins: coins,
      terrainType: TerrainType.Rochoso,
    };

    return (this.cell = new Cell(propsCell));
  }

  createCoins(probability: rangeProbability, valueMaxCoins: number): number {
    let valueCoin = new Array<number>();

    for (let i = 0; i <= probability; i = i + 0.1) {
      valueCoin.push(
        Math.floor(Math.random() * valueMaxCoins) *
          Math.floor(Math.random() * 2)
      );
    }

    return valueCoin[Math.floor(Math.random() * valueCoin.length)];
  }
}
