import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { SignInComponent } from './signin/sign-in.component';
import { SignUpComponent } from './signin/sign-up.component';
//import { HomeComponent } from './home/home.component';

const appRoutes: Routes = [
  { path: '', component: SignInComponent },
  { path: 'login', component: SignInComponent },
  { path: 'signup', component: SignUpComponent },
  //{ path: 'home', component: HomeComponent },
/* { path: 'groups', component: GroupsComponent,
    children: [
    { path: ':id', component: GroupComponent },
    { path: ':id/edit', component: EditGroupComponent }
  ] },*/
  { path: 'not-found', component: PageNotFoundComponent },
  { path: '**', redirectTo: '/not-found' }
];

@NgModule({
  imports: [
    RouterModule.forRoot(appRoutes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {

}
