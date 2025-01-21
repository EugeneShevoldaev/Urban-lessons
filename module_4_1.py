from fake_math import divide as fake_div
from true_math import divide as true_div

resolt_fake = fake_div(3, 0)
print(f'fake_div: -  {resolt_fake}')

resolt_true = true_div(15, 0)
print(f'true_div: -  {resolt_true}')
