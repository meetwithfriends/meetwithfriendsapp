import { Injectable } from '@angular/core';
import { Headers, Http, Response } from '@angular/http';
import 'rxjs/Rx';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class ServerService {

  serverUrl = "http://localhost:5000/"
  constructor(private http: Http) {}
  signUp(request) {
    const headers = new Headers({'Content-Type': 'application/json'});
    return this.http.post(this.serverUrl + 'signup', request, {headers: headers})
      .map(
        (response: Response) => {
          console.log(response.json());
        }
      )
      .catch(
        (error: Response) => {
          return Observable.throw('Something went wrong');
        }
      );
  }
/*  getServers() {
    return this.http.get('https://udemy-ng-http.firebaseio.com/data')
      .map(
        (response: Response) => {
          const data = response.json();
          for (const server of data) {
            server.name = 'FETCHED_' + server.name;
          }
          return data;
        }
      )
      .catch(
        (error: Response) => {
          return Observable.throw('Something went wrong');
        }
      );
  }
  getAppName() {
    return this.http.get('https://udemy-ng-http.firebaseio.com/appName.json')
      .map(
        (response: Response) => {
          return response.json();
        }
      );
  }*/
}
