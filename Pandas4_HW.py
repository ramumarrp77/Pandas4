##PANDAS HW 4 Solutions


# Problem 1 : Nth Highest Salary


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(salary) < N or N <=0 :
        return pd.DataFrame([None],columns = [f'getNthHighestSalary({N})'])
    else:
        Nthsalary = salary.iloc[N-1]
        return pd.DataFrame([Nthsalary], columns = [f'getNthHighestSalary({N})'])






# Problem 2 : Second Highest Salary

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salary = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(salary) > 1:
        secondsal = salary.iloc[1]
        return pd.DataFrame([secondsal],columns=['SecondHighestSalary'])
    else:
        return pd.DataFrame([None],columns = ['SecondHighestSalary'])