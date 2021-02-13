import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IceCreamsComponent } from './ice-creams.component';

describe('IceCreamsComponent', () => {
  let component: IceCreamsComponent;
  let fixture: ComponentFixture<IceCreamsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ IceCreamsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(IceCreamsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
