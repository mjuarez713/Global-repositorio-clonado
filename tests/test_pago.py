import unittest
from flask import current_app
from app import create_app
from app.models.pagos import Pago

class PagoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
 
    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_pago(self):
        pago = Pago()
        pago.fechapago = '10'
        pago.monto = '7000'
        pago.tipopago = 'efectivo'
        self.assertTrue(pago.fechapago, '10')
        self.assertTrue(pago.monto, '7000')
        self.assertTrue(pago.tipopago, 'efectivo')

if __name__ == "__main__":
    unittest.main()
  
