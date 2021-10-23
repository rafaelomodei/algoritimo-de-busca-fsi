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
    this.spawnScenary(1, 10);
  }

  spawnScenary(lines: number, columns: number): void {
    console.log('line: ', lines, 'width: ', columns);

    let index = 0;

    for (let x = 0; x < lines; x++) {
      for (let y = 0; y < columns; y++) {

        
        const coins = this.createCoins(PROBABILITYCREATECOINS, VALUEMAXCOINS);
        const currentReference = this.createCell(index, x, y, coins);

        console.log(` --- [${ x } , ${ y }] ---  index: ${index}`);
        console.log('NEW currentReference: ', currentReference);




        
        if(this.referenceMatrix === undefined) {
            this.referenceMatrix = currentReference;

            this.headerReferenceColumn = this.referenceMatrix;
            this.headerReferenceLine = this.referenceMatrix;

            this.currentReferenceColumn = this.referenceMatrix;
            this.currentReferenceLine = this.referenceMatrix;

  
            console.log('-------------------');
            console.log('CREATE::referenceMatrix: ', this.referenceMatrix);
            console.log('CREATE::headerReferenceColumn: ', this.headerReferenceColumn);
            console.log('CREATE::headerReferenceLine: ', this.headerReferenceLine);
            console.log('CREATE::currentReferenceColumn: ', this.currentReferenceColumn);
            console.log('CREATE::currentReferenceLine: ', this.currentReferenceLine);
            console.log('-------------------');
        }


        currentReference.left = this.currentReferenceColumn.right;
        this.currentReferenceColumn.right = currentReference;
 


        console.log('-------------------');
        console.log('currentReference: ', currentReference);
        console.log('currentReference::left: ', currentReference.left);
        console.log('currentReference::right: ', currentReference.right);
        console.log('currentReferenceColumn: ', this.currentReferenceColumn);
        console.log('currentReferenceColumn::left: ', this.currentReferenceColumn.left);
        console.log('currentReferenceColumn::right: ', this.currentReferenceColumn.right);

        // console.log('currentReferenceColumn::right: ', this.currentReferenceColumn.right);
        // console.log('currentReference::left: ', currentReference.left);

        console.log('-------------------');
        index++;



        // else{

        //     if(y === 1){
        //       this.headerReferenceLine.right = currentReference;
        //     }
        //     // if(currentReference.right === this.headerReferenceLine){
              
        //     // }
            
        //     this.headerReferenceLine.left = currentReference;
        //     currentReference.left = this.currentReferenceColumn;
        //     // currentReference.up = this.headerReferenceLine;

        //     currentReference.right = this.headerReferenceLine;
        //     // currentReference.down = this.headerReferenceColumn;

        //     // this.currentReferenceColumn.right = currentReference;
        //     // this.currentReferenceLine.up = currentReference;

        //     this.currentReferenceColumn.right = currentReference;
        //     this.currentReferenceColumn = currentReference;

        //     // this.currentReferenceLine = currentReference;
            
        //     // console.log('currentReference::up: ', currentReference.up);
        //     console.log('currentReference::right: ', currentReference.right);
        //     // console.log('currentReference::down: ', currentReference.down);

        //     // console.log('currentReferenceColumn::right: ', this.currentReferenceColumn.right);
        //     console.log('currentReferenceColumn: ', this.currentReferenceColumn);
        //     console.log('currentReferenceColumn::left: ', this.currentReferenceColumn.left);
        //     console.log('currentReferenceColumn::right: ', this.currentReferenceColumn.right);



        //     // console.log('currentReferenceLine::up ', this.currentReferenceLine.up);
        //     // console.log('currentReferenceLine: ', this.currentReferenceLine);

        //     console.log('headerReferenceLine: ', this.headerReferenceLine);
        //     console.log('headerReferenceLine::left ', this.headerReferenceLine.left);
        //     console.log('headerReferenceLine::right ', this.headerReferenceLine.right);




        //     console.log('-------------------');
  
        // }

        // if(x > 0){
        //   currentReference.up = this.currentReferenceLine;
        //   this.currentReferenceLine.down = currentReference;

        // }

  
      //   console.log(` --- INICIO - LINES ---  [${ x } , ${ y }] `);

      //   const coins = this.createCoins(PROBABILITYCREATECOINS, VALUEMAXCOINS);
      //   const currentReference = this.createCell(index, x, y, coins);
      //   index++;

      //   currentReference.left = this.currentReferenceLine;
      //   this.currentReferenceLine.right = currentReference;
      //   this.currentReferenceLine = currentReference;
      //   console.log('Lines::currentReference: ', currentReference);
      //   console.log('Lines::currentReferenceLine::right: ', this.currentReferenceLine.right);
      //   console.log('Lines::currentReferenceLine: ', this.currentReferenceLine);
      //   console.log(' --- FIM - LINES ---');

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
