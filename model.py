from sqlalchemy import Column, Sequence, Integer, String
from config import BASE


class TestRecords(BASE):

    __tablename__ = 'test_records'
    test_record_id = Column(Integer(11), Sequence('test_records_id_sequence'), 
        primary_key=True, nullable=False)
    test_type = Column(String(255), nullable=False)


    test_billing_firstname = Column(String(255))
    test_billing_lastname = Column(String(255))
    test_billing_company = Column(String(255))
    test_billing_email = Column(String(255))
    test_billing_address1 = Column(String(255))
    test_billing_address2 = Column(String(255))
    test_billing_city = Column(String(255))
    test_billing_state = Column(String(255))
    test_billing_postal_code = Column(String(255))
    test_billing_country = Column(String(255))
    test_billing_telephone = Column(String(255))

    test_shipping_firstname = Column(String(255))
    test_shipping_lastname = Column(String(255))
    test_shipping_company = Column(String(255))
    test_shipping_address1 = Column(String(255))
    test_shipping_address2 = Column(String(255))
    test_shipping_city = Column(String(255))
    test_shipping_state = Column(String(255))
    test_shipping_postal_code = Column(String(255))
    test_shipping_country = Column(String(255))
    test_shipping_telephone = Column(String(255))