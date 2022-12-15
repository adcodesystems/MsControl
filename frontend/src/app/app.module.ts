import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { NgModel } from '@angular/forms';
import { CommonModule } from '@angular/common';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PersonaNaturalFormComponent } from './components/persona-natural-form/persona-natural-form.component';
import { PreloginComponent } from './components/prelogin/prelogin.component';
import { LoginComponent } from './components/login/login.component';
import { SetupMarcacionComponent } from './components/setup-marcacion/setup-marcacion.component';

import { FormsModule } from '@angular/forms';

import { MarcacionComponent } from './components/marcacion/marcacion.component';

import { PersonaService } from './services/persona.service';
import { TipoconfiguracionComponent } from './components/tipoconfiguracion/tipoconfiguracion.component';
import { TipoconfiguracionmarcacionComponent } from './components/tipoconfiguracionmarcacion/tipoconfiguracionmarcacion.component';
import { TipoConfiguracionMarcacionService } from './services/tipoconfiguracionmarcacion.service';
import { MenuComponent } from './components/menu/menu.component';
import { PageHomeComponent } from './components/page-home/page-home.component';



@NgModule({
  declarations: [
    AppComponent,
    PersonaNaturalFormComponent,
    PreloginComponent,
    LoginComponent,
    SetupMarcacionComponent,
    MarcacionComponent,
    TipoconfiguracionComponent,
    TipoconfiguracionmarcacionComponent,
    MenuComponent,
    PageHomeComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    CommonModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [PersonaService, TipoConfiguracionMarcacionService],
  bootstrap: [AppComponent]
})
export class AppModule { }
