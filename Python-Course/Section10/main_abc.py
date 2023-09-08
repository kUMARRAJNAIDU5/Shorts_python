from FulltimeEmployee import FulltimeEmployee
from FulltimeEmployee import ContractEmployee
from FulltimeEmployee import Payroll

payroll = Payroll()

payroll.add(FulltimeEmployee('John', 'Doe', 6000))
payroll.add(FulltimeEmployee('Jane', 'Doe', 6500))
payroll.add(ContractEmployee('Jenifer', 'Smith', 200, 50))
payroll.add(ContractEmployee('David', 'Wilson', 150, 100))
payroll.add(ContractEmployee('Kevin', 'Miller', 100, 150))

payroll.print()