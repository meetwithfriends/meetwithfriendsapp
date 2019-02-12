import { Component } from '@angular/core';
import { Response } from '@angular/http';

import { ServerService } from './../server.service';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css']
})
export class SignInComponent {

  constructor(private serverService: ServerService) {}
  onSignInClick(email: string, pass: string) {
    let x = {"email": email, "pass": pass};
    this.serverService.signIn(JSON.stringify(x))
      .subscribe(
        (response) => console.log(response),
        (error) => console.log(error)
      );
  }
  onLogIn() {
    this.serverService.signUp('22')
      .subscribe(
        (response) => console.log(response),
        (error) => console.log(error)
      );
  }
}
