import { Component } from '@angular/core';
import { Response } from '@angular/http';

import { ServerService } from './../server.service';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent {

  constructor(private serverService: ServerService) {}
  onSignUpClick(email: string, pass: string) {
    let x = {"email": email, "pass": pass};
    this.serverService.signUp(JSON.stringify(x))
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
