import { Component, HostBinding, OnInit } from '@angular/core';
import { TipoConfiguracionMarcacionModel } from 'src/app/Models/TipoConfiguracionMarcacionModel';

import { TipoConfiguracionMarcacionService } from '../../services/tipoconfiguracionmarcacion.service';
import { Router } from '@angular/router'

@Component({
  selector: 'app-tipoconfiguracionmarcacion',
  templateUrl: './tipoconfiguracionmarcacion.component.html',
  styleUrls: ['./tipoconfiguracionmarcacion.component.css']
})
export class TipoconfiguracionmarcacionComponent implements OnInit {

  @HostBinding('class') classes = 'row';
  edit: boolean = false;

  model_tip_config_mar: TipoConfiguracionMarcacionModel = {
    TIP_CON_MARID: 0,
    TIP_CON_MAR: ''
  }
  TipoConfiguracionMarcaciones: any = []

  constructor(protected tipoconfiguracionmarcacionservices: TipoConfiguracionMarcacionService, private router: Router) { }

  ngOnInit() {

    this.Get_TipoConfiguracionMarcacion();
  }

  Insert_TipoConfiguracionMarcacion() {
    this.tipoconfiguracionmarcacionservices.Insert_TipoConfiguracionMarcacion(this.model_tip_config_mar)
      .subscribe(
        res => {
          console.log(res);
          this.Get_TipoConfiguracionMarcacion();
          this.model_tip_config_mar = {
            TIP_CON_MARID: 0,
            TIP_CON_MAR: ''
          }
          // this.router.navigate(['/persona']);
        },
        err => console.error(err)
      )
  }

  Get_TipoConfiguracionMarcacion() {
    this.tipoconfiguracionmarcacionservices.Get_TipoConfiguracionMarcacion().subscribe(
      res => { this.TipoConfiguracionMarcaciones = res; },
      err => console.error
    );
  }



  Delete_TipoConfiguracionMarcacion(Id: number) {
    this.tipoconfiguracionmarcacionservices.Delete_TipoConfiguracionMarcacion(Id)
      .subscribe(
        res => {
          console.log(res);
          this.Get_TipoConfiguracionMarcacion();
        },
        err => console.error(err)
      )
  }

 
  Update_TipoConfiguracionMarcacion() {
    this.tipoconfiguracionmarcacionservices.Update_TipoConfiguracionMarcacion(this.model_tip_config_mar)
      .subscribe(
        res => {
          console.log(res);
          this.Get_TipoConfiguracionMarcacion();
          this.model_tip_config_mar = {
            TIP_CON_MARID: 0,
            TIP_CON_MAR: ''
          }
          this.edit = false
          // this.router.navigate(['/persona']);
        },
        err => console.error(err)
      )
  }



}

