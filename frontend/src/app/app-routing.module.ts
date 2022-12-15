import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { PersonaNaturalFormComponent } from './components/persona-natural-form/persona-natural-form.component';
import { MarcacionComponent } from './components/marcacion/marcacion.component';
import { TipoconfiguracionmarcacionComponent } from './components/tipoconfiguracionmarcacion/tipoconfiguracionmarcacion.component';
import { PageHomeComponent } from './components/page-home/page-home.component';
import { SetupMarcacionComponent } from './components/setup-marcacion/setup-marcacion.component';
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
  {
    path:'Home',
    component: PageHomeComponent
  },{
    path:'SetupMarcacion',
    component: SetupMarcacionComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule {

}
