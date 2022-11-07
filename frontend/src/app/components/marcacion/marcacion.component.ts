import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-marcacion',
  templateUrl: './marcacion.component.html',
  styleUrls: ['./marcacion.component.css']
})
export class MarcacionComponent implements OnInit {

  colorbody="black;";
  prueba="red;"
  // arr_color={
  //   "background:":this.colorbody,
  // }

  constructor() { }

  // IniciarJornada(){
  //   this.colorbody='#ff4848;';
    // this.colorbody="linear-gradient(to bottom right, #ff4848, #F00000);";
    // this.arr_color["background:"]=this.colorbody;
  // }


  ngOnInit(): void {
  }



}
