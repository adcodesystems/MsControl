import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { NgModel } from '@angular/forms';
import { CommonModule } from '@angular/common';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PersonaNaturalFormComponent } from './components/persona-natural-form/persona-natural-form.component';
import { PreloginComponent } from './components/prelogin/prelogin.component';
import { LoginComponent } from './components/login/login.component';
import { SetupMarcacionComponent } from './components/setup-marcacion/setup-marcacion.component';

import { MarcacionComponent } from './components/marcacion/marcacion.component';


@NgModule({
  declarations: [
    AppComponent,
    PersonaNaturalFormComponent,
    PreloginComponent,
    LoginComponent,
    SetupMarcacionComponent,
    MarcacionComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    CommonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
