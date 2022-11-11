import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-marcacion',
  templateUrl: './marcacion.component.html',
  styleUrls: ['./marcacion.component.css']
})
export class MarcacionComponent implements OnInit {

  colorbody:string="red";

  constructor() { }

  ngOnInit(): void {
  }

  changecolor(){
    this.colorbody="blue";
  }


}
