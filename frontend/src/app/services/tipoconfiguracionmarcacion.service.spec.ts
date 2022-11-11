import { TestBed } from '@angular/core/testing';
import { TipoConfiguracionMarcacionService } from './tipoconfiguracionmarcacion.service';

describe('TipoConfiguracionMarcacionService', () => {
  let service: TipoConfiguracionMarcacionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TipoConfiguracionMarcacionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
