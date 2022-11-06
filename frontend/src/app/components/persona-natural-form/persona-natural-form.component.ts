import { Component, HostBinding, OnInit } from '@angular/core';
import { PersonaModel } from 'src/app/Models/PersonaModel';

import { PersonaService } from '../../services/persona.service';
import { Router } from '@angular/router'

@Component({
  selector: 'app-persona-natural-form',
  templateUrl: './persona-natural-form.component.html',
  styleUrls: ['./persona-natural-form.component.css']
})
export class PersonaNaturalFormComponent implements OnInit {

  @HostBinding('class') classes = 'row';
  edit: boolean = false;

  person: PersonaModel = {
    PERID: 0,
    DOC_PER: '',
    NOM_PER: '',
    APE_PAT: '',
    APE_MAT: ''
  }
  Personas: any = []

  constructor(protected personasservices: PersonaService, private router: Router) { }

  ngOnInit() {

    this.GetPersonas();
  }

  SaveNewPersona() {
    this.personasservices.PersonasaveGame(this.person)
      .subscribe(
        res => {
          console.log(res);
          this.GetPersonas();
          this.person = {
            PERID: 0,
            DOC_PER: '',
            NOM_PER: '',
            APE_PAT: '',
            APE_MAT: ''
          }
          // this.router.navigate(['/persona']);
        },
        err => console.error(err)
      )
  }

  GetPersonas() {
    this.personasservices.getPersonas().subscribe(
      res => { this.Personas = res; },
      err => console.error
    );
  }



  DeleteNewPersona(Id: number) {
    this.personasservices.PersonaDelete(Id)
      .subscribe(
        res => {
          console.log(res);
          this.GetPersonas();
        },
        err => console.error(err)
      )
  }

  UpdateNewPersona(Data: any) {
    this.person = Data
    this.edit = true
    // this.personasservices.PersonasaveGame(this.person)
    //   .subscribe(
    //     res => {
    //       console.log(res);
    //       this.GetPersonas();
    //       this.person = {
    //         PERID: 0,
    //         DOC_PER: '',
    //         NOM_PER: '',
    //         APE_PAT: '',
    //         APE_MAT: ''
    //       }
    //       // this.router.navigate(['/persona']);
    //     },
    //     err => console.error(err)
    //   )
  }
  UpdateTotalNewPersona() {
    this.personasservices.PersonasUpdate(this.person)
      .subscribe(
        res => {
          console.log(res);
          this.GetPersonas();
          this.person = {
            PERID: 0,
            DOC_PER: '',
            NOM_PER: '',
            APE_PAT: '',
            APE_MAT: ''
          }
          this.edit = false
          // this.router.navigate(['/persona']);
        },
        err => console.error(err)
      )
  }



}
