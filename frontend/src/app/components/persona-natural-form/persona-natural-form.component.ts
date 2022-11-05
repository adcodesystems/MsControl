import { Component, OnInit } from '@angular/core';

import { PersonaService } from '../../services/persona.service';
import {PersonaModel} from '../../Models/PersonaModel';

@Component({
  selector: 'app-persona-natural-form',
  templateUrl: './persona-natural-form.component.html',
  styleUrls: ['./persona-natural-form.component.css']
})
export class PersonaNaturalFormComponent implements OnInit {

  Personas: any = []

  constructor(protected personasservices: PersonaService) { }

  ngOnInit() {

    this.personasservices.getPersonas().subscribe(
      res => { this.Personas = res; },
      err => console.error
    );
  }

}
