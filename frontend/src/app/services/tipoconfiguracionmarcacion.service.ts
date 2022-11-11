import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { TipoConfiguracionMarcacionModel } from '../Models/TipoConfiguracionMarcacionModel';

@Injectable({
  providedIn: 'root'
})
export class TipoConfiguracionMarcacionService {
  API_URI = 'http://localhost:4000'

  constructor(private http: HttpClient) { }

  Get_TipoConfiguracionMarcacion() {
    return this.http.get(`${this.API_URI}/Get_TipoConfiguracionMarcacionItems`)
  }
  Insert_TipoConfiguracionMarcacion(model_tip_config_mar: TipoConfiguracionMarcacionModel) {
    return this.http.post(`${this.API_URI}/Post_TipoConfiguracionMarcacion_Insert`, model_tip_config_mar);
  }

  Delete_TipoConfiguracionMarcacion(Id: number) {
    return this.http.delete(`${this.API_URI}/Post_TipoConfiguracionMarcacion_Delete/${Id}`);
  }
  Update_TipoConfiguracionMarcacion(model_tip_config_mar: TipoConfiguracionMarcacionModel) {
    return this.http.post(`${this.API_URI}/Update_TipoConfiguracionMarcacion_Insert`, model_tip_config_mar);
  }

}
