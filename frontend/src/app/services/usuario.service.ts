import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
// import { PersonaModel } from '../Models/PersonaModel';


@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  API_URI = 'http://localhost:4000'

  constructor(private http: HttpClient) { }

  GetAcceso(usu:string,pwd :string) {
    return this.http.get(`${this.API_URI}/Usuario/GetAcceso/${usu}/${pwd}`);
  }
 
}
