import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import {} from '../Models/PersonaModel';

@Injectable({
  providedIn: 'root'
})
export class PersonaService {
  API_URI='http://localhost:4000'

  constructor(private http: HttpClient) { }

  getPersonas(){
return this.http.get(`${this.API_URI}/Get_PersonaNaturalItems`)  

  }
}
