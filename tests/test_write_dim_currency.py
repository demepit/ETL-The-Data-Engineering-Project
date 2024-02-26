from src.utils.writing_utils.write_dim_currency import write_dim_currency 
# from src.utils.writing_utils.get_secret import get_secret 
from datetime import datetime as dt
import pytest
from unittest.mock import Mock
from awswrangler import _utils
pg8000 = _utils.import_optional_dependency("pg8000")
from pg8000.native import Connection, literal, identifier, DatabaseError


@pytest.mark.describe('write_dim_currency()')
@pytest.mark.it('correct_data_is_written_to_DB')
def test_correct_data_is_written_to_DB():
    data = [
        {'currency_id': 1, 'currency_code': 'GBP', 'currency_name': 'British Pound'},
        {'currency_id': 2, 'currency_code': 'USD', 'currency_name': 'US Dollar'},
        {'currency_id': 3, 'currency_code': 'EUR', 'currency_name': 'Euro'}
    ]
    con = Mock()
    mock_datetime = dt(2024, 2, 26, 10, 30, 0)
    write_dim_currency(con, data, mock_datetime )
    assert con.run.call_count == len(data)
    
    
    
    
    # for call_args, expected_query in zip(mock_connection.run.call_args_list, expected_queries):
    #     assert call_args[0][0] == expected_quer
    # expected = [f"""
    #     INSERT INTO dim_currency
    #     VALUES
    #     (1,1,'GBP','British Pound','2024-02-26','10:30:0:0')
    #     INSERT INTO dim_currency
    #     VALUES
    #     (2,2,'USD','US Dollar','2024-02-26','10:30:0:0')
    #     INSERT INTO dim_currency
    #     VALUES
    #     (3,3,'EUR','Euro','2024-02-26','10:30:0:0')
    #     ON CONFLICT DO NOTHING;
    #     """ ]