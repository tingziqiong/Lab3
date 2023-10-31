import employee_info

employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]


def test_get_employees_by_age_range():
    lower_limit = 30
    upper_limit = 40

    result = employee_info.get_employees_by_age_range(lower_limit,upper_limit)
    test = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]

    assert (result == test)


def test_calculate_average_salary():
    result = round(employee_info.calculate_average_salary(),2)
    test = 60166.67

    assert (result == test)


def test_get_employees_by_dept():
    department = "Marketing"

    result = employee_info.get_employees_by_dept(department)
    test = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]

    assert (result == test)