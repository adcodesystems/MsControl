import { Component, OnInit } from '@angular/core';

import { PersonaService } from '../../services/persona.service';

@Component({
  selector: 'app-persona-natural-form',
  templateUrl: './persona-natural-form.component.html',
  styleUrls: ['./persona-natural-form.component.css']
})
export class PersonaNaturalFormComponent implements OnInit {

  constructor(private personaservice: PersonaService) { }

  ngOnInit(): void {

    // this.personaservice.getPersonas().subscribe(
    //   res => console.log(res),
    //   err => console.error
    // );
  }

}
