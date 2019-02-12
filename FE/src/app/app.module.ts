import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { SignInComponent } from './signin/sign-in.component';
import { SignUpComponent } from './signin/sign-up.component';
//import { ForgotPasswordComponent } from './signin/forgot-password.component';
//import { HomeComponent } from './home/home.component';

import { AppRoutingModule } from './app-router.module';
import { ServerService } from './server.service';

@NgModule({
  declarations: [
    AppComponent,
    PageNotFoundComponent,
    SignInComponent,
    SignUpComponent
    //HomeComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AppRoutingModule
  ],
  providers: [ServerService],
  bootstrap: [AppComponent]
})
export class AppModule { }
