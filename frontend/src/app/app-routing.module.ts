import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { PersonaNaturalFormComponent } from './components/persona-natural-form/persona-natural-form.component';
import { MarcacionComponent } from './components/marcacion/marcacion.component';
import { TipoconfiguracionmarcacionComponent } from './components/tipoconfiguracionmarcacion/tipoconfiguracionmarcacion.component';

const routes: Routes = [
  {
    path: '',
    component: LoginComponent,
    pathMatch:'full'
  },
  {
    path: 'marcacion',
    component: MarcacionComponent
  },
  {
    path:'Persona',
    component: PersonaNaturalFormComponent
  },
  {
    path:'TipoConfiguracionMarcacion',
    component: TipoconfiguracionmarcacionComponent
  },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule {

}
