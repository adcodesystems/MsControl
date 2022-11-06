import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PersonaNaturalFormComponent } from './components/persona-natural-form/persona-natural-form.component';
import { PreloginComponent } from './components/prelogin/prelogin.component';
import { LoginComponent } from './components/login/login.component';
import { SetupMarcacionComponent } from './components/setup-marcacion/setup-marcacion.component';

import { FormsModule } from '@angular/forms';

import { MarcacionComponent } from './components/marcacion/marcacion.component';

import { PersonaService } from './services/persona.service';



@NgModule({
  declarations: [
    AppComponent,
    PersonaNaturalFormComponent,
    PreloginComponent,
    LoginComponent,
    SetupMarcacionComponent,
    MarcacionComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule

  ],
  providers: [PersonaService],
  bootstrap: [AppComponent]
})
export class AppModule { }
