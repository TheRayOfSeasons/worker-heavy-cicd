import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { FlavorsComponent } from './pages/flavors/flavors.component';
import { HomeComponent } from './pages/home/home.component';
import { IceCreamsComponent } from './pages/ice-creams/ice-creams.component';

const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'ice-creams', component: IceCreamsComponent },
  {path: 'flavors', component: FlavorsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
