#write functions here, don't add input('') statements here!

def test_config():
    return True


def create_multiplication_table(row, col):
    
    table = []
    for i in range(row):
        row_values = [(i + 1) * (j + 1) for j in range(col)]
        table.append(row_values)

        
    return table
