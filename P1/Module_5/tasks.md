## Task Requirements:

### Test 1: Valid Formats (Parametrized)

- Use `@pytest.mark.parametrize`.

- Arguments: raw_input, expected_output.

- Cases to cover:

    - "12/01/2023" $\rightarrow$ "2023-12-01" 
    
    - 1"2023.12.01" $\rightarrow$ "2023-12-01" 
    
    - 2"01/30/2020" $\rightarrow$ "2020-01-30" (Checking non-ambiguous days)

### Test 2: Invalid Formats (Exception Handling)

- Write a separate test function test_invalid_dates.

- Use parametrization to test multiple bad inputs.

- Cases: 

    - "invalid", "2023/12/01" (slashes YMD not supported), "13/01/2023" (Month 13 impossible).
    
    - Assert: The code must raise ValueError3.