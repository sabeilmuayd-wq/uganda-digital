import pandas as pd
def get_mock_data():
    return pd.DataFrame({
        'Parish': ['Bweyale', 'Kiryandongo', 'Mutunda'],
        'Active Hives': [120, 85, 200]
    })
